import logging
import requests

logger = logging.getLogger(__name__)


class APIClient(requests.Session):
    """
    Base API client class
    """

    def __init__(self, base_url: str):
        """
        :param base_url: Base url of the service.
        """
        self._base_url = base_url
        super().__init__()

    def request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """
        Send API request to an endpoint

        :param method: HTTP method (uppercase)
        :param endpoint: API endpoint
        :param kwargs: additional request arguments. The same as in `requests.request <https://requests.readthedocs.io/en/latest/api/#requests.request>`_.
        Includes params, data, json, headers, cookies. timeout, allow_redirects, verify and more
        :return: HTTP response object
        """
        url = self._base_url + endpoint
        logger.debug('Making request: %s %s', method, url)
        response = super().request(method, url, **kwargs)
        logger.debug('Request finished: %s %s', response.request.method, response.request.url)
        logger.debug('Request headers: %s', response.request.headers)

        if response.request.body:
            logger.debug('Request body: %s', response.request.body)

        logger.debug('Response code: %s', response.status_code)
        logger.debug('Response headers: %s', response.headers)

        if response.text:
            logger.debug('Response body: %s', response.text)

        return response

    def get(self, endpoint: str, **kwargs):
        return self.request('GET', endpoint, **kwargs)
