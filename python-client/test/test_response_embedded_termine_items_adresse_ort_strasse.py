"""
    Arbeitsagentur Ausbildungssuche API

    Eine der größten Ausbildungsdatenbanken Deutschlands durchsuchen.   Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:  **ClientID:** 1c852184-1944-4a9e-a093-5cc078981294  **ClientSecret:** 777f9915-9f0d-4982-9c33-07b5810a3e79.   **Achtung**: der generierte Token muss bei folgenden GET-requests im header als 'OAuthAccessToken' inkludiert werden.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.ausbildungssuche.model.response_embedded_termine_items_adresse_ort_strasse_koordinaten import (
    ResponseEmbeddedTermineItemsAdresseOrtStrasseKoordinaten,
)
from deutschland.ausbildungssuche.model.response_embedded_termine_items_angebot_bildungsanbieter_adresse_ort_strasse_land import (
    ResponseEmbeddedTermineItemsAngebotBildungsanbieterAdresseOrtStrasseLand,
)

from deutschland import ausbildungssuche

globals()[
    "ResponseEmbeddedTermineItemsAdresseOrtStrasseKoordinaten"
] = ResponseEmbeddedTermineItemsAdresseOrtStrasseKoordinaten
globals()[
    "ResponseEmbeddedTermineItemsAngebotBildungsanbieterAdresseOrtStrasseLand"
] = ResponseEmbeddedTermineItemsAngebotBildungsanbieterAdresseOrtStrasseLand
from deutschland.ausbildungssuche.model.response_embedded_termine_items_adresse_ort_strasse import (
    ResponseEmbeddedTermineItemsAdresseOrtStrasse,
)


class TestResponseEmbeddedTermineItemsAdresseOrtStrasse(unittest.TestCase):
    """ResponseEmbeddedTermineItemsAdresseOrtStrasse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseEmbeddedTermineItemsAdresseOrtStrasse(self):
        """Test ResponseEmbeddedTermineItemsAdresseOrtStrasse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ResponseEmbeddedTermineItemsAdresseOrtStrasse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
