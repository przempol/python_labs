def parse_input(input):
    """
    Splits multiline string into list of lists with integers.

    Napisz funkcję przymującą wielolinijkowy ciąg znaków.
    a zwracającą listę list liczb całkowitych znajdujących się w podanym ciągu znaków.
    Nie używaj pętl for i while.
    String może zawierać puste linie na początku i końcu.

    :param input: string to parse
    :type input: str
    :return: list of parsed list of integers
    :rtype: list
    """

    ret = input.strip()  # deleting white chars
    ret = ret.splitlines()  # putting into one list
    ret = list(map(lambda x: x.split(' '), ret))
    ret = list(map(lambda x: list(map(lambda x_y: int(x_y), x)), ret))  # x stand for lists in list, x_y is elem. of x
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
assert parse_input(_input) == [[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]
