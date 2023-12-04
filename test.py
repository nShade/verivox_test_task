import requests
import yaml
from pytest import mark
from http import HTTPStatus


HOST = 'https://service.verivox.de/'
GET_CITIES = 'geo/latestv2/cities/{POSTCODE}'
GET_STREETS = '/geo/latestv2/cities/{POSTCODE}/{CITY}/streets'

with open('config.yaml') as config_file:
    config = yaml.safe_load(config_file)


@mark.parametrize('postcode, cities', [
    (postcode['value'], [city['name']
                         for city in postcode['cities']])
    for postcode in config['postcodes']
])
def test_get_cities(postcode, cities):
    """
    GIVEN the address checking service endpoint: https://service.verivox.de/geo/latestv2/cities/POSTCODE
    WHEN I request the cities for postcode {10409}
         https://service.verivox.de/geo/latestv2/cities/10409/
    THEN I should receive a response with only one city: Berlin
    """
    resp = requests.get(HOST + GET_CITIES.format(POSTCODE=postcode))
    assert resp.status_code == HTTPStatus.OK
    assert resp.json() == {'Cities': cities}


@mark.parametrize('postcode', [
    22333
])
def test_get_cities_not_found(postcode):
    resp = requests.get(HOST + GET_CITIES.format(POSTCODE=postcode))
    assert resp.status_code == HTTPStatus.NOT_FOUND
    assert resp.content == b''


@mark.parametrize('postcode, city, streets', [
    (postcode['value'], city['name'], city['streets'])
    for postcode in config['postcodes'] for city in postcode['cities']
])
def test_get_streets(postcode, city, streets):
    """
    GIVEN the address checking service endpoint: https://service.verivox.de/geo/latestv2/cities/
    WHEN I request the streets for {Berlin} postcode {10409}
            https://service.verivox.de/geo/latestv2/cities/10409/Berlin/streets
    THEN I should receive a response with 29 streets
    """
    resp = requests.get(HOST + GET_STREETS.format(POSTCODE=postcode, CITY=city))
    assert resp.status_code == HTTPStatus.OK
    assert resp.json() == {'Streets': streets}
