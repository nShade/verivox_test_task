from api_wrapper.agent import APIAgent


class AddressCheckingServiceClient(APIAgent):

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
