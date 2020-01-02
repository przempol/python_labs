import requests
import socket


API_URL = 'https://www.metaweather.com/api/'


def get_cities_woeid(query: str, timeout: float = 5.) -> dict:
    try:
        response = requests.get(url="https://www.metaweather.com/api/location/search/?query={}".format(query)
                                , timeout=timeout)
    except socket.timeout:
        raise requests.exceptions.Timeout
    if response.status_code != 200:
        raise requests.exceptions.HTTPError

    try:
        ret: dict = {doc["title"]: doc["woeid"] for doc in response.json()}
    except Exception:
        raise RuntimeError

    return ret


if __name__ == '__main__':
    assert get_cities_woeid('Warszawa') == {}
    assert get_cities_woeid('War') == {
        'Warsaw': 523920,
        'Newark': 2459269,
    }
    try:
        get_cities_woeid('Warszawa', 0.1)
    except Exception as exc:
        isinstance(exc, requests.exceptions.Timeout)
