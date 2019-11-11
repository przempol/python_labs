"""
Uzupełnij klasę Calculator o obsługę wyjątków (1pkt).
Podnoszone wyjątki:
- błędna operacja - WrongOperation
- błędne argumenty (nie liczba) - NotNumberArgument
- pusta pamięć (zarówno przy pytaniu o pamięć
jak i operację z argumentem domyślnym) - EmptyMemory
- dzielenie przez zero jest przekształcane w CalculatorError
"""
from operator import add, mul, sub, truediv


class CalculatorError(Exception):
    def __init__(self):
        try:
            a = 1 / 0
        except Exception as e:
            self.__cause__ = e
        print("Dividing by 0 (cries in math)")


class WrongOperation(CalculatorError):
    def __init__(self):
        print("Wrong operation")


class NotNumberArgument(CalculatorError):
    def __init__(self):
        print("Argument is not a number")


class EmptyMemory(CalculatorError):
    def __init__(self):
        print("Empty memory")


class Calculator:
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv,
    }

    def __init__(self):
        self._memory = None
        self._short_memory = None

    def run(self, operator, arg1, arg2=None):
        """
        Returns result of given operation.

        :param operator: sign of operation to perform
        :type operator: str
        :param arg1: first argument, must be a numeric value
        :type arg1: float
        :param arg2: optional, second argument, must be a numeric value
        :type arg2: float
        :return: result of operation
        :rtype: float
        """
        if operator in self.operations:
            if arg2 is None and self.memory is None:
                raise EmptyMemory
            elif arg2 == 0 and operator == "/":
                raise CalculatorError
            elif type(arg1) != (float, int) or type(arg2) != (float, int):
                raise NotNumberArgument
            else:
                arg2 = arg2 or self.memory
                # checking for non-zero argument
                if arg2:
                    self._short_memory = self.operations[operator](arg1, arg2)
                    return self._short_memory
                else:
                    raise EmptyMemory from ZeroDivisionError
        else:
            raise WrongOperation

    @property
    def memory(self):
        return self._memory

    def memorize(self):
        """Saves last operation result to memory."""
        self._memory = self._short_memory

    def clean_memory(self):
        """Cleans memorized value"""
        self._memory = None

    def in_memory(self):
        """Prints memorized value."""
        if self.memory is not None:
            print(f"Memorized value: {self.memory}")
        else:
            raise EmptyMemory


if __name__ == '__main__':
    b = None
    calc = Calculator()

    try:
        b = calc.run('+', 1, 'a')
    except CalculatorError as exc:
        assert type(exc) == NotNumberArgument
        assert b is None

    try:
        b = calc.run('^', 2, 3)
    except CalculatorError as exc:
        assert type(exc) == WrongOperation
        assert b is None

    try:
        calc.in_memory()
    except CalculatorError as exc:
        assert type(exc) is EmptyMemory
    else:
        raise AssertionError

    try:
        b = calc.run('/', 2)
    except CalculatorError as exc:
        assert type(exc) == EmptyMemory
        assert b is None
    else:
        raise AssertionError

    try:
        b = calc.run('/', 1, 0)
    except CalculatorError as exc:
        assert type(exc.__cause__) == ZeroDivisionError
        assert b is None
    else:
        raise AssertionError
