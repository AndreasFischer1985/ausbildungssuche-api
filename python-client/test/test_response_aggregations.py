"""
    Arbeitsagentur Ausbildungssuche API

    Eine der größten Ausbildungsdatenbanken Deutschlands durchsuchen.   Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:  **ClientID:** 1c852184-1944-4a9e-a093-5cc078981294  **ClientSecret:** 777f9915-9f0d-4982-9c33-07b5810a3e79.   **Achtung**: der generierte Token muss bei folgenden GET-requests im header als 'OAuthAccessToken' inkludiert werden.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.ausbildungssuche.model.response_aggregations_anbieter import (
    ResponseAggregationsANBIETER,
)
from deutschland.ausbildungssuche.model.response_aggregations_anzahlausgefiltert import (
    ResponseAggregationsANZAHLAUSGEFILTERT,
)
from deutschland.ausbildungssuche.model.response_aggregations_anzahlgesamt import (
    ResponseAggregationsANZAHLGESAMT,
)
from deutschland.ausbildungssuche.model.response_aggregations_beginntermin import (
    ResponseAggregationsBEGINNTERMIN,
)
from deutschland.ausbildungssuche.model.response_aggregations_bildungsarten import (
    ResponseAggregationsBILDUNGSARTEN,
)
from deutschland.ausbildungssuche.model.response_aggregations_integrationstypen import (
    ResponseAggregationsINTEGRATIONSTYPEN,
)
from deutschland.ausbildungssuche.model.response_aggregations_regionen import (
    ResponseAggregationsREGIONEN,
)
from deutschland.ausbildungssuche.model.response_aggregations_schulabschluesse import (
    ResponseAggregationsSCHULABSCHLUESSE,
)
from deutschland.ausbildungssuche.model.response_aggregations_unterrichtsformen import (
    ResponseAggregationsUNTERRICHTSFORMEN,
)
from deutschland.ausbildungssuche.model.response_aggregations_vorbereitendehilfentypen import (
    ResponseAggregationsVORBEREITENDEHILFENTYPEN,
)

from deutschland import ausbildungssuche

globals()["ResponseAggregationsANBIETER"] = ResponseAggregationsANBIETER
globals()[
    "ResponseAggregationsANZAHLAUSGEFILTERT"
] = ResponseAggregationsANZAHLAUSGEFILTERT
globals()["ResponseAggregationsANZAHLGESAMT"] = ResponseAggregationsANZAHLGESAMT
globals()["ResponseAggregationsBEGINNTERMIN"] = ResponseAggregationsBEGINNTERMIN
globals()["ResponseAggregationsBILDUNGSARTEN"] = ResponseAggregationsBILDUNGSARTEN
globals()[
    "ResponseAggregationsINTEGRATIONSTYPEN"
] = ResponseAggregationsINTEGRATIONSTYPEN
globals()["ResponseAggregationsREGIONEN"] = ResponseAggregationsREGIONEN
globals()["ResponseAggregationsSCHULABSCHLUESSE"] = ResponseAggregationsSCHULABSCHLUESSE
globals()[
    "ResponseAggregationsUNTERRICHTSFORMEN"
] = ResponseAggregationsUNTERRICHTSFORMEN
globals()[
    "ResponseAggregationsVORBEREITENDEHILFENTYPEN"
] = ResponseAggregationsVORBEREITENDEHILFENTYPEN
from deutschland.ausbildungssuche.model.response_aggregations import (
    ResponseAggregations,
)


class TestResponseAggregations(unittest.TestCase):
    """ResponseAggregations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseAggregations(self):
        """Test ResponseAggregations"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ResponseAggregations()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
