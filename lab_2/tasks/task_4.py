def count_letters(msg):
    dict = {}
    ret1 = 'a'
    ret2 = 0
    for c in msg:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    for c in dict:
        if dict[c] > ret2:
            ret2 = dict[c]
            ret1 = c
        elif dict[c] == ret2 and c < ret1:
            ret1 = c
    ret = (ret1, ret2)
    return ret

    """
    Zwraca pare (znak, liczba zliczeń) dla najczęściej występującego znaku w wiadomości.
    W przypadku równości zliczeń wartości sortowane są alfabetycznie.

    :param msg: Message to count chars in.
    :type msg: str
    :return: Most frequent pair char - count in message.
    :rtype: list
    """
    pass


if __name__ == '__main__':
    msg = 'Abrakadabra'
    assert count_letters(msg) == ('a', 4)
    assert count_letters('za') == ('a', 1)