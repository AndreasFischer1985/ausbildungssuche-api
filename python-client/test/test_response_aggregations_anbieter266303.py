"""
    Arbeitsagentur Ausbildungssuche API

    Eine der größten Ausbildungsdatenbanken Deutschlands durchsuchen.   Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:  **ClientID:** 1c852184-1944-4a9e-a093-5cc078981294  **ClientSecret:** 777f9915-9f0d-4982-9c33-07b5810a3e79.   **Achtung**: der generierte Token muss bei folgenden GET-requests im header als 'OAuthAccessToken' inkludiert werden.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.ausbildungssuche.model.response_aggregations_anbieter266303 import (
    ResponseAggregationsANBIETER266303,
)

from deutschland import ausbildungssuche


class TestResponseAggregationsANBIETER266303(unittest.TestCase):
    """ResponseAggregationsANBIETER266303 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseAggregationsANBIETER266303(self):
        """Test ResponseAggregationsANBIETER266303"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ResponseAggregationsANBIETER266303()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()