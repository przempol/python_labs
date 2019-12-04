import numpy as np


def calculate_neighbours(board):
    """
    Returns number of neighbours of board cells.

    Funkcja zwraca tablicę która w polu [R, C] zwraca liczbę sąsiadów którą
    ma komórka board[R, C].
    Obowiązuje sąsiedztwo Moore'a tzn. za sąsiada uznajemy żywą komórkę
    stykającą się bokiem bokach lub na ukos od danej komórki,
    więc maksymalna ilość sąsiadów danej komórki wynosi 8.
    Funkcja ta powinna być zwektoryzowana, tzn. liczba operacji w bytecodzie
    Pythona nie powinna zależeć od rozmiaru macierzy.
    (1 pkt.)

    Podpowiedź: Czy jest możliwe obliczenie ilości np. lewych sąsiadów
    których ma każda z komórek w macierzy, następnie liczby prawych sąsiadów
    itp.
    Podpowiedź II: Proszę uważać na komówki na bokach i rogach planszy.

    :param board: 2D array of agents states.
    :type board: np.ndarray
    :param periodic
    """
    # game of life
    # tez bez for'ów!!
    # komorki po przekatnych tez sa sasiadami
    ret = np.zeros(shape=board.shape, dtype=int)
    ret[:, :-1] += board[:, 1:]
    ret[:, 1:] += board[:, :-1]
    ret[:-1, :] += board[1:, :]
    ret[1:, :] += board[:-1, :]
    ret[1:, 1:] += board[:-1, :-1]
    ret[:-1, :-1] += board[1:, 1:]
    ret[1:, :-1] += board[:-1, 1:]
    ret[:-1, 1:] += board[1:, :-1]

    return ret


def iterate(board):
    """
    Returns next iteration step of given board.

    Funkcja pobiera planszę game of life i zwraca jej następną iterację.
    Zasady Game of life są takie:
    1. Komórka może być albo żywa (True) albo martwa (False).
    2. Jeśli komórka jest martwa i ma trzech sąsiadów to ożywa.
    3. Jeśli komórka jest żywa i ma mniej niż dwóch sąsiadów to umiera,
       jeśli ma więcej niż trzech sąsiadów również umiera.
       W przeciwnym wypadku (dwóch lub trzech sąsiadów) to żyje dalej.
    (1 pkt.)

    :param board: 2D array of agents states.
    :type board: np.ndarray
    :return: next board state
    :rtype: np.ndarray
    """
    number_of_neighbors = calculate_neighbours(board)
    is_alive = board
    is_dead = np.invert(board)

    second_rule = (number_of_neighbors == 3) & is_dead

    third_rule = (2 <= number_of_neighbors) & (number_of_neighbors <= 3)

    return second_rule | (third_rule & is_alive)


if __name__ == '__main__':
    _board = np.array([
        [False, False, False, True, False, True],
        [True, False, True, False, False, True],
        [True, True, False, True, True, True],
        [False, True, True, False, False, True],
        [False, False, False, True, False, False],
        [False, True, True, True, False, True]
    ])
    assert (calculate_neighbours(_board) == np.array([
        [1, 2, 2, 1, 3, 1, ],
        [2, 4, 3, 4, 6, 3, ],
        [3, 5, 5, 3, 4, 3, ],
        [3, 3, 4, 4, 5, 2, ],
        [2, 4, 6, 3, 4, 2, ],
        [1, 1, 3, 2, 3, 0, ],
    ])).all()
    assert (iterate(_board) == np.array([
        [False, False, False, False, True, False],
        [True, False, True, False, False, True],
        [True, False, False, True, False, True],
        [True, True, False, False, False, True],
        [False, False, False, True, False, False],
        [False, False, True, True, True, False],
    ])).all()
