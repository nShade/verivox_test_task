import requests
from pytest import mark, fixture, FixtureRequest
from http import HTTPStatus

GET_CITIES = 'geo/latestv2/cities/{POSTCODE}'
GET_STREETS = '/geo/latestv2/cities/{POSTCODE}/{CITY}/streets'


@fixture
def streets(request: FixtureRequest, config):
    postcode = request.getfixturevalue('postcode')
    city = request.getfixturevalue('city')

    return next((c['streets']
                 for c in next((p['cities']
                                for p in config['postcodes']
                                if str(p['value']) == str(postcode)))
                 if c['name'] == city))


@mark.parametrize('postcode, cities', [
    ('10409', ['Berlin']),
    ('77716', ['Fischerbach', 'Haslach', 'Hofstetten']),
])
def test_get_cities(postcode, cities, host):
    """
    GIVEN the address checking service endpoint: https://service.verivox.de/geo/latestv2/cities/POSTCODE
    WHEN I request the cities for postcode {10409}
         https://service.verivox.de/geo/latestv2/cities/10409/
    THEN I should receive a response with only one city: Berlin
    """
    resp = requests.get(host + GET_CITIES.format(POSTCODE=postcode))
    assert resp.status_code == HTTPStatus.OK
    assert resp.json() == {'Cities': cities}


@mark.parametrize('postcode', [
    '22333'
])
def test_get_cities_not_found(postcode, host):
    resp = requests.get(host + GET_CITIES.format(POSTCODE=postcode))
    assert resp.status_code == HTTPStatus.NOT_FOUND
    assert resp.content == b''


@mark.parametrize('postcode, city', [
    ('10409', 'Berlin'),
    ('77716', 'Fischerbach'),
    ('77716', 'Haslach'),
    ('77716', 'Hofstetten'),
])
def test_get_streets(postcode, city, streets, host):
    """
    GIVEN the address checking service endpoint: https://service.verivox.de/geo/latestv2/cities/
    WHEN I request the streets for {Berlin} postcode {10409}
            https://service.verivox.de/geo/latestv2/cities/10409/Berlin/streets
    THEN I should receive a response with 29 streets
    """
    resp = requests.get(host + GET_STREETS.format(POSTCODE=postcode, CITY=city))
    assert resp.status_code == HTTPStatus.OK
    assert resp.json() == {'Streets': streets}
