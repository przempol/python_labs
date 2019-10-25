from task_1 import parse_input
import collections

def check_frequency(input):
    """
    Perform counting based on input queries and return queries result.

    Na wejściu otrzymujemy parę liczb całkowitych - operacja, wartość.
    Możliwe operacje:
    1, x: zlicz x
    2, x: usuń jedno zliczenie x jeżeli występuje w zbiorze danych
    3, x: wypisz liczbę zliczeń x (0 jeżeli nie występuje)
    Do parsowania wejścia wykorzystaj funkcję parse_input.
    Zbiór danych zrealizuj za pomocą struktury z collections.

    :param input: pairs of int: command, value
    :type input: string
    :return: list of integers with results of operation 3
    :rtype: list
    """
    data = parse_input(input)   # parsing input
    counter = collections.Counter() # collections for task
    ret = []

    for ii in range(len(data)):
        if data[ii][0] == 1:
            counter.update([data[ii][1]])
        elif data[ii][0] == 2 and data[ii][1] in counter.keys():
            counter[data[ii][1]] = counter[data[ii][1]] - 1
        elif data[ii][0] == 3:
            print(counter[data[ii][1]])
            ret.append(counter[data[ii][1]])    # adding result to return
    print(ret)
    return ret


_input = """
1 5
1 6
3 2
1 10
1 10
1 6
2 5
3 2


"""
assert check_frequency(_input) == [0, 0]