# Author: Suprith Gangawar <sgangawa@redhat.com>

import datetime
import json

import requests
import pytest

def url_builder(city_id):
    user_api = 'd2d5fd8339f931608f25273e333ee45d'
    unit = 'metric'
    api = "https://api.openweathermap.org/data/2.5/forecast?q="
    full_api_url = api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url


def data_fetch(full_api_url):
    url = requests.get(full_api_url)
    print(url.url)
    raw_api_dict = json.loads(url.text)
    return raw_api_dict


def compare_date(date):
    t = datetime.datetime.now().date().today()
    today_date = datetime.datetime.strptime(t.strftime("%Y-%m-%d"), "%Y-%m-%d")
    given_date = datetime.datetime.strptime(date.split()[0], '%Y-%m-%d')
    if (given_date - today_date).days == 1:
        return True
    else:
        return False

@pytest.mark.parametrize('country', ['London', 'Newyork', 'India'])
def test_api_call(country):
# url_builder() function takes an entry from list and modifies the URL accordingly.
    uri = url_builder(country)
    data = data_fetch(uri)
    data_len = len(data['list'])
    for i in range(data_len):
        if compare_date(data['list'][i]['dt_txt']):
            assert data['list'][i]['main']['temp_max'] < 10

