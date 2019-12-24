import tkinter as tk
from functools import partial
from lab_9.tools.calculator import Calculator, CalculatorError, EmptyMemory


class CalculatorGUI(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.variables = {}
        self.state = tk.BooleanVar(value=True)
        self.init_variables()
        self.calculator = Calculator()

        self.screen = tk.Label(self, bg='white')
        self.screen.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.bottom_pad = self.init_bottom_pad()
        self.bottom_pad.pack(side=tk.BOTTOM)

    def init_variables(self):
        self.variables['var_1'] = ''
        self.variables['var_2'] = ''
        self.variables['operator'] = ''
        self.state.set(True)
        self.variables['decimals_1'] = 0
        self.variables['decimals_2'] = 0
        self.variables['is_float'] = False

    def init_bottom_pad(self):
        bottom_pad = tk.Frame(self)

        # klawiatura numeryczna
        num_pad = tk.Frame(bottom_pad)
        num_pad.pack(side=tk.LEFT)
        num_positions = [(4, 1), (3, 1), (3, 2), (3, 3), (2, 1), (2, 2), (2, 3), (0, 1), (0, 2), (0, 3)]
        functions = [(0, 0, 'MC', self.calculator.clean_memory), (2, 0, 'MR', self.memory_read),
                     (3, 0, 'M+', self.calculator.memorize), (4, 0, 'C', self.clear),
                     (4, 2, '.', self.coma), (4, 3, '=', self.calculate_result)]
        number: int = 0
        for row, col in num_positions:
            tk.Button(
                num_pad, text=number, width=5,
                command=partial(self.update_var, number)
            ).grid(row=row, column=col)
            number += 1

        for ii in range(5):
            tk.Label(num_pad, text="- -").grid(row=1, column=ii)

        for row, col, text, func in functions:
            tk.Button(num_pad, text=text, width=5, command=func).grid(row=row, column=col)

        tmp_table = [0, 2, 3, 4]    # for the purpose of task 3 look
        for ii, operation in enumerate(self.calculator.operations.keys()):
            tk.Button(num_pad, text=operation, width=5, command=partial(self.set_operator, operation),
                      ).grid(row=tmp_table[ii], column=4)
        return bottom_pad

    def update_screen(self):
        text = f"{self.variables['var_1']}"
        if self.variables['operator']:
            text += f" {self.variables['operator']}"
        if self.variables['var_2']:
            text += f" {self.variables['var_2']}"
        self.screen['text'] = text

    def clear(self):
        state = self.state.get()
        self.variables['is_float'] = False
        if state:
            self.variables['var_1'] = ''
            self.variables['decimals_1'] = 0
        else:
            self.variables['var_2'] = ''
            self.variables['decimals_2'] = 0
        self.update_screen()

    def update_var(self, num):
        state = self.state.get()
        if state:
            self.variables['var_1'] += str(num)
            self.variables['var_1'] = self.variables['var_1'].lstrip('0')
            if self.variables['is_float']:
                self.variables['decimals_1'] += 1
        else:
            self.variables['var_2'] += str(num)
            self.variables['var_2'] = self.variables['var_2'].lstrip('0')
            if self.variables['is_float']:
                self.variables['decimals_2'] += 1
        self.update_screen()

    def set_operator(self, operator):
        if self.variables['var_1']:
            self.variables['is_float'] = False
            self.variables['operator'] = operator
            self.state.set(not self.state.get())
            self.update_screen()

    def calculate_result(self):
        if self.variables['var_1'] and self.variables['var_2']:
            var_1 = float(self.variables['var_1'])
            var_2 = float(self.variables['var_2'])
            if self.variables['decimals_1'] > 0 or self.variables['decimals_2'] > 0:
                if self.variables['operator'] == '/':
                    self.screen['text'] = self.calculator.run(
                        self.variables['operator'], var_1, var_2
                    )
                else:
                    self.screen['text'] = round(self.calculator.run(
                        self.variables['operator'], var_1, var_2
                    ), self.variables['decimals_1'] + self.variables['decimals_2'])
            else:
                if self.variables['operator'] == '/':
                    self.screen['text'] = self.calculator.run(
                        self.variables['operator'], var_1, var_2
                    )
                else:
                    self.screen['text'] = int(self.calculator.run(
                        self.variables['operator'], var_1, var_2
                    ))
            self.init_variables()

    def memory_read(self):
        try:
            self.update_var(self.calculator.memory)
            if self.state.get():
                self.variables['decimals_1'] = len(str(self.calculator.memory).split('.')[1])
            else:
                self.variables['decimals_2'] = len(str(self.calculator.memory).split('.')[1])
        except CalculatorError as exc:
            if type(exc) is EmptyMemory:
                pass

    def coma(self):
        self.update_var('.')
        self.variables['is_float'] = True

    def key(self, event):
        for ii in range(0, 10):
            if event.char == str(ii):
                self.update_var(ii)

        if event.char == '.':
            self.coma()

        if event.char == '\r':
            self.calculate_result()

        if event.char in ['+', '-', '*', '/']:
            self.set_operator(event.char)


if __name__ == '__main__':
    root = tk.Tk()
    CalculatorGUI(root).pack()
    root.mainloop()
