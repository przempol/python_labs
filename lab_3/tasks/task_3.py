"""
Zadanie za 2 pkt.
Uzupełnij funckję parse_dates tak by zwracała przygotowaną wiadomość
z posortowanymi zdarzeniami.
Funkcja przyjmuje ciag zdarzeń (zapisanych w formie timestampu w dowolnej strefie czasowej),
przetwarza je na zdarzenia w strefie czasowej UTC i sortuje.
Posortowane zdarzenia są grupowane na dni i wypisywane od najnowszych do najstarszych.
Na 1pkt. Uzupełnij funkcję sort_dates, która przyjmuje dwa parametry:
- log (wielolinijkowy ciąg znaków z datami) zdarzeń
- format daty (podany w assercie format ma być domyślnym)
Zwraca listę posortowanych obiektów typu datetime w strefie czasowej UTC.
Funkcje group_dates oraz format_day mają pomoc w grupowaniu kodu.
UWAGA: Proszę ograniczyć użycie pętli do minimum.
"""
import datetime as dt
import pytz

#### PLEASE READ
#### PLEASE READ
#### PLEASE READ
#### PLEASE READ
#### PLEASE READ
#### PLEASE READ
# final output was hardcoded to match assert (once was tabulator, once was four spaces :<)

def string_to_dt(string):
    dt_obj = dt.datetime.strptime(string, '%a %d %b %Y %X %z') # using dt and pytz functions to return good output
    dt_obj = dt_obj.astimezone(pytz.utc)
    return dt_obj


def parse_dates(date_str, date_format=''):
    """
    Parses and groups (in UTC) given list of events.
    :param date_str: log of events in time
    :type date_str: str
    :param date_format: event format
    :type date_format: str
    :return: parsed events
    :rtype: str
    """
    dates_list = date_str.strip()  # deleting general white chars
    dates_list = dates_list.splitlines()  # putting into one list
    dates_list = list(map(lambda x: x.strip(), dates_list))  # deleting white chars in every date
    dates_list = list(map(lambda x: string_to_dt(x), dates_list))  # applying function changing string to dt object
    dates_list.sort(reverse=True)
    current_day = dates_list[0].strftime("%Y-%m-%d")
    ret = current_day
    #loop for matching output in assertion (once was 4 spaces, once was tabulator)
    for ii in range(len(dates_list)):
        if dates_list[ii].strftime("%Y-%m-%d") != current_day:
            ret = ret + '\n    ----'
            current_day = dates_list[ii].strftime("%Y-%m-%d")
            ret = ret + '\n    '
            ret = ret + current_day
        ret = ret + '\n    '
        ret = ret + dates_list[ii].strftime("\t%X")
    ret = ret
    return ret


if __name__ == '__main__':
    dates = """
    Sun 10 May 2015 13:54:36 -0700
    Sun 10 May 2015 13:54:36 -0000
    Sat 02 May 2015 19:54:36 +0530
    Fri 01 May 2015 13:54:36 -0000
    """

    assert parse_dates(dates) == """2015-05-10
    \t20:54:36
    \t13:54:36
    ----
    2015-05-02
    \t14:24:36
    ----
    2015-05-01
    \t13:54:36"""