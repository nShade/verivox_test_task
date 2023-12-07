from api_client.base_client import APIClient


class AddressCheckingServiceClient(APIClient):

    def get_cities(self, postcode, **kwargs):
        """
        GET /geo/latestv2/cities/{postcode}

        Get list of cities by postcode
        """
        return self.get(f'/geo/latestv2/cities/{postcode}', **kwargs)

    def get_streets(self, postcode, city, **kwargs):
        """
        GET /geo/latestv2/cities/{postcode}/{city}/streets

        Get list of streets by postcode and city name
        """
        return self.get(f'/geo/latestv2/cities/{postcode}/{city}/streets', **kwargs)
