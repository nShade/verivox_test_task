from pytest import mark, fixture, FixtureRequest
from http import HTTPStatus


@fixture
def streets(request: FixtureRequest, config):
    postcode = request.getfixturevalue('postcode')
    city = request.getfixturevalue('city')
    return config['streets'][int(postcode)][city]


@mark.parametrize('postcode, cities', [
    ('10409', ['Berlin']),
    ('77716', ['Fischerbach', 'Haslach', 'Hofstetten']),
])
def test_get_cities(postcode, cities, api_client):
    """
    GIVEN Address checking service
    WHEN  User requests from the service cities by valid postcode {postcode}
    THEN  The service returns list of cities {cities} to which this postcode area belongs
    """
    resp = api_client.get_cities(postcode=postcode)
    assert resp.status_code == HTTPStatus.OK
    assert resp.json() == {'Cities': cities}


def test_get_cities_not_found(api_client):
    """
    GIVEN Address checking service
    WHEN  User requests from the service cities by invalid postcode {postcode}
    THEN  The service returns HTTP code 404
    """
    INVALID_POSTCODE = '22333'
    resp = api_client.get_cities(postcode=INVALID_POSTCODE)
    assert resp.status_code == HTTPStatus.NOT_FOUND
    assert resp.content == b''


@mark.parametrize('postcode, city', [
    ('10409', 'Berlin'),
    ('77716', 'Fischerbach'),
    ('77716', 'Haslach'),
    ('77716', 'Hofstetten'),
])
def test_get_streets(postcode, city, streets, api_client):
    """
    GIVEN Address checking service
    WHEN  User requests from the service streets by valid postcode {postcode} and city name {city}
    THEN  The service returns list of streets {streets} located in this postcode area and city
    """
    resp = api_client.get_streets(postcode=postcode, city=city)
    assert resp.status_code == HTTPStatus.OK
    assert resp.json() == {'Streets': streets}
