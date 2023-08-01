"""
    Arbeitsagentur Ausbildungssuche API

    Eine der größten Ausbildungsdatenbanken Deutschlands durchsuchen.   Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:  **ClientID:** 1c852184-1944-4a9e-a093-5cc078981294  **ClientSecret:** 777f9915-9f0d-4982-9c33-07b5810a3e79.   **Achtung**: der generierte Token muss bei folgenden GET-requests im header als *'OAuthAccessToken'* inkludiert werden. Alternativ kann man bei folgenden GET-requests auch direkt die *client_id* als Header-Parameter *'X-API-Key'* übergeben - *'OAuthAccessToken'* ist in diesem Fall nicht erforderlich. 🚀   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: andreasfischer1985@web.de
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.ausbildungssuche.exceptions import ApiAttributeError
from deutschland.ausbildungssuche.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    OpenApiModel,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)


def lazy_import():
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin0 import (
        ResponseAggregationsBEGINNTERMIN0,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin1 import (
        ResponseAggregationsBEGINNTERMIN1,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin2 import (
        ResponseAggregationsBEGINNTERMIN2,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin101 import (
        ResponseAggregationsBEGINNTERMIN101,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin102 import (
        ResponseAggregationsBEGINNTERMIN102,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin103 import (
        ResponseAggregationsBEGINNTERMIN103,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin104 import (
        ResponseAggregationsBEGINNTERMIN104,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin105 import (
        ResponseAggregationsBEGINNTERMIN105,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin106 import (
        ResponseAggregationsBEGINNTERMIN106,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin107 import (
        ResponseAggregationsBEGINNTERMIN107,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin108 import (
        ResponseAggregationsBEGINNTERMIN108,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin109 import (
        ResponseAggregationsBEGINNTERMIN109,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin110 import (
        ResponseAggregationsBEGINNTERMIN110,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin111 import (
        ResponseAggregationsBEGINNTERMIN111,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin112 import (
        ResponseAggregationsBEGINNTERMIN112,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin113 import (
        ResponseAggregationsBEGINNTERMIN113,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin201 import (
        ResponseAggregationsBEGINNTERMIN201,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin202 import (
        ResponseAggregationsBEGINNTERMIN202,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin203 import (
        ResponseAggregationsBEGINNTERMIN203,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin204 import (
        ResponseAggregationsBEGINNTERMIN204,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin205 import (
        ResponseAggregationsBEGINNTERMIN205,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin206 import (
        ResponseAggregationsBEGINNTERMIN206,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin207 import (
        ResponseAggregationsBEGINNTERMIN207,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin208 import (
        ResponseAggregationsBEGINNTERMIN208,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin209 import (
        ResponseAggregationsBEGINNTERMIN209,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin210 import (
        ResponseAggregationsBEGINNTERMIN210,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin211 import (
        ResponseAggregationsBEGINNTERMIN211,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin212 import (
        ResponseAggregationsBEGINNTERMIN212,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin301 import (
        ResponseAggregationsBEGINNTERMIN301,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin302 import (
        ResponseAggregationsBEGINNTERMIN302,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin303 import (
        ResponseAggregationsBEGINNTERMIN303,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin304 import (
        ResponseAggregationsBEGINNTERMIN304,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin305 import (
        ResponseAggregationsBEGINNTERMIN305,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin306 import (
        ResponseAggregationsBEGINNTERMIN306,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin307 import (
        ResponseAggregationsBEGINNTERMIN307,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin308 import (
        ResponseAggregationsBEGINNTERMIN308,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin309 import (
        ResponseAggregationsBEGINNTERMIN309,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin310 import (
        ResponseAggregationsBEGINNTERMIN310,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin311 import (
        ResponseAggregationsBEGINNTERMIN311,
    )
    from deutschland.ausbildungssuche.model.response_aggregations_beginntermin312 import (
        ResponseAggregationsBEGINNTERMIN312,
    )

    globals()["ResponseAggregationsBEGINNTERMIN0"] = ResponseAggregationsBEGINNTERMIN0
    globals()["ResponseAggregationsBEGINNTERMIN1"] = ResponseAggregationsBEGINNTERMIN1
    globals()[
        "ResponseAggregationsBEGINNTERMIN101"
    ] = ResponseAggregationsBEGINNTERMIN101
    globals()[
        "ResponseAggregationsBEGINNTERMIN102"
    ] = ResponseAggregationsBEGINNTERMIN102
    globals()[
        "ResponseAggregationsBEGINNTERMIN103"
    ] = ResponseAggregationsBEGINNTERMIN103
    globals()[
        "ResponseAggregationsBEGINNTERMIN104"
    ] = ResponseAggregationsBEGINNTERMIN104
    globals()[
        "ResponseAggregationsBEGINNTERMIN105"
    ] = ResponseAggregationsBEGINNTERMIN105
    globals()[
        "ResponseAggregationsBEGINNTERMIN106"
    ] = ResponseAggregationsBEGINNTERMIN106
    globals()[
        "ResponseAggregationsBEGINNTERMIN107"
    ] = ResponseAggregationsBEGINNTERMIN107
    globals()[
        "ResponseAggregationsBEGINNTERMIN108"
    ] = ResponseAggregationsBEGINNTERMIN108
    globals()[
        "ResponseAggregationsBEGINNTERMIN109"
    ] = ResponseAggregationsBEGINNTERMIN109
    globals()[
        "ResponseAggregationsBEGINNTERMIN110"
    ] = ResponseAggregationsBEGINNTERMIN110
    globals()[
        "ResponseAggregationsBEGINNTERMIN111"
    ] = ResponseAggregationsBEGINNTERMIN111
    globals()[
        "ResponseAggregationsBEGINNTERMIN112"
    ] = ResponseAggregationsBEGINNTERMIN112
    globals()[
        "ResponseAggregationsBEGINNTERMIN113"
    ] = ResponseAggregationsBEGINNTERMIN113
    globals()["ResponseAggregationsBEGINNTERMIN2"] = ResponseAggregationsBEGINNTERMIN2
    globals()[
        "ResponseAggregationsBEGINNTERMIN201"
    ] = ResponseAggregationsBEGINNTERMIN201
    globals()[
        "ResponseAggregationsBEGINNTERMIN202"
    ] = ResponseAggregationsBEGINNTERMIN202
    globals()[
        "ResponseAggregationsBEGINNTERMIN203"
    ] = ResponseAggregationsBEGINNTERMIN203
    globals()[
        "ResponseAggregationsBEGINNTERMIN204"
    ] = ResponseAggregationsBEGINNTERMIN204
    globals()[
        "ResponseAggregationsBEGINNTERMIN205"
    ] = ResponseAggregationsBEGINNTERMIN205
    globals()[
        "ResponseAggregationsBEGINNTERMIN206"
    ] = ResponseAggregationsBEGINNTERMIN206
    globals()[
        "ResponseAggregationsBEGINNTERMIN207"
    ] = ResponseAggregationsBEGINNTERMIN207
    globals()[
        "ResponseAggregationsBEGINNTERMIN208"
    ] = ResponseAggregationsBEGINNTERMIN208
    globals()[
        "ResponseAggregationsBEGINNTERMIN209"
    ] = ResponseAggregationsBEGINNTERMIN209
    globals()[
        "ResponseAggregationsBEGINNTERMIN210"
    ] = ResponseAggregationsBEGINNTERMIN210
    globals()[
        "ResponseAggregationsBEGINNTERMIN211"
    ] = ResponseAggregationsBEGINNTERMIN211
    globals()[
        "ResponseAggregationsBEGINNTERMIN212"
    ] = ResponseAggregationsBEGINNTERMIN212
    globals()[
        "ResponseAggregationsBEGINNTERMIN301"
    ] = ResponseAggregationsBEGINNTERMIN301
    globals()[
        "ResponseAggregationsBEGINNTERMIN302"
    ] = ResponseAggregationsBEGINNTERMIN302
    globals()[
        "ResponseAggregationsBEGINNTERMIN303"
    ] = ResponseAggregationsBEGINNTERMIN303
    globals()[
        "ResponseAggregationsBEGINNTERMIN304"
    ] = ResponseAggregationsBEGINNTERMIN304
    globals()[
        "ResponseAggregationsBEGINNTERMIN305"
    ] = ResponseAggregationsBEGINNTERMIN305
    globals()[
        "ResponseAggregationsBEGINNTERMIN306"
    ] = ResponseAggregationsBEGINNTERMIN306
    globals()[
        "ResponseAggregationsBEGINNTERMIN307"
    ] = ResponseAggregationsBEGINNTERMIN307
    globals()[
        "ResponseAggregationsBEGINNTERMIN308"
    ] = ResponseAggregationsBEGINNTERMIN308
    globals()[
        "ResponseAggregationsBEGINNTERMIN309"
    ] = ResponseAggregationsBEGINNTERMIN309
    globals()[
        "ResponseAggregationsBEGINNTERMIN310"
    ] = ResponseAggregationsBEGINNTERMIN310
    globals()[
        "ResponseAggregationsBEGINNTERMIN311"
    ] = ResponseAggregationsBEGINNTERMIN311
    globals()[
        "ResponseAggregationsBEGINNTERMIN312"
    ] = ResponseAggregationsBEGINNTERMIN312


class ResponseAggregationsBEGINNTERMIN(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {}

    validations = {}

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (
            bool,
            date,
            datetime,
            dict,
            float,
            int,
            list,
            str,
            none_type,
        )  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            "_0": (ResponseAggregationsBEGINNTERMIN0,),  # noqa: E501
            "_1": (ResponseAggregationsBEGINNTERMIN1,),  # noqa: E501
            "_2": (ResponseAggregationsBEGINNTERMIN2,),  # noqa: E501
            "_101": (ResponseAggregationsBEGINNTERMIN101,),  # noqa: E501
            "_102": (ResponseAggregationsBEGINNTERMIN102,),  # noqa: E501
            "_103": (ResponseAggregationsBEGINNTERMIN103,),  # noqa: E501
            "_104": (ResponseAggregationsBEGINNTERMIN104,),  # noqa: E501
            "_105": (ResponseAggregationsBEGINNTERMIN105,),  # noqa: E501
            "_106": (ResponseAggregationsBEGINNTERMIN106,),  # noqa: E501
            "_107": (ResponseAggregationsBEGINNTERMIN107,),  # noqa: E501
            "_108": (ResponseAggregationsBEGINNTERMIN108,),  # noqa: E501
            "_109": (ResponseAggregationsBEGINNTERMIN109,),  # noqa: E501
            "_110": (ResponseAggregationsBEGINNTERMIN110,),  # noqa: E501
            "_111": (ResponseAggregationsBEGINNTERMIN111,),  # noqa: E501
            "_112": (ResponseAggregationsBEGINNTERMIN112,),  # noqa: E501
            "_113": (ResponseAggregationsBEGINNTERMIN113,),  # noqa: E501
            "_201": (ResponseAggregationsBEGINNTERMIN201,),  # noqa: E501
            "_202": (ResponseAggregationsBEGINNTERMIN202,),  # noqa: E501
            "_203": (ResponseAggregationsBEGINNTERMIN203,),  # noqa: E501
            "_204": (ResponseAggregationsBEGINNTERMIN204,),  # noqa: E501
            "_205": (ResponseAggregationsBEGINNTERMIN205,),  # noqa: E501
            "_206": (ResponseAggregationsBEGINNTERMIN206,),  # noqa: E501
            "_207": (ResponseAggregationsBEGINNTERMIN207,),  # noqa: E501
            "_208": (ResponseAggregationsBEGINNTERMIN208,),  # noqa: E501
            "_209": (ResponseAggregationsBEGINNTERMIN209,),  # noqa: E501
            "_210": (ResponseAggregationsBEGINNTERMIN210,),  # noqa: E501
            "_211": (ResponseAggregationsBEGINNTERMIN211,),  # noqa: E501
            "_212": (ResponseAggregationsBEGINNTERMIN212,),  # noqa: E501
            "_301": (ResponseAggregationsBEGINNTERMIN301,),  # noqa: E501
            "_302": (ResponseAggregationsBEGINNTERMIN302,),  # noqa: E501
            "_303": (ResponseAggregationsBEGINNTERMIN303,),  # noqa: E501
            "_304": (ResponseAggregationsBEGINNTERMIN304,),  # noqa: E501
            "_305": (ResponseAggregationsBEGINNTERMIN305,),  # noqa: E501
            "_306": (ResponseAggregationsBEGINNTERMIN306,),  # noqa: E501
            "_307": (ResponseAggregationsBEGINNTERMIN307,),  # noqa: E501
            "_308": (ResponseAggregationsBEGINNTERMIN308,),  # noqa: E501
            "_309": (ResponseAggregationsBEGINNTERMIN309,),  # noqa: E501
            "_310": (ResponseAggregationsBEGINNTERMIN310,),  # noqa: E501
            "_311": (ResponseAggregationsBEGINNTERMIN311,),  # noqa: E501
            "_312": (ResponseAggregationsBEGINNTERMIN312,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "_0": "0",  # noqa: E501
        "_1": "1",  # noqa: E501
        "_2": "2",  # noqa: E501
        "_101": "101",  # noqa: E501
        "_102": "102",  # noqa: E501
        "_103": "103",  # noqa: E501
        "_104": "104",  # noqa: E501
        "_105": "105",  # noqa: E501
        "_106": "106",  # noqa: E501
        "_107": "107",  # noqa: E501
        "_108": "108",  # noqa: E501
        "_109": "109",  # noqa: E501
        "_110": "110",  # noqa: E501
        "_111": "111",  # noqa: E501
        "_112": "112",  # noqa: E501
        "_113": "113",  # noqa: E501
        "_201": "201",  # noqa: E501
        "_202": "202",  # noqa: E501
        "_203": "203",  # noqa: E501
        "_204": "204",  # noqa: E501
        "_205": "205",  # noqa: E501
        "_206": "206",  # noqa: E501
        "_207": "207",  # noqa: E501
        "_208": "208",  # noqa: E501
        "_209": "209",  # noqa: E501
        "_210": "210",  # noqa: E501
        "_211": "211",  # noqa: E501
        "_212": "212",  # noqa: E501
        "_301": "301",  # noqa: E501
        "_302": "302",  # noqa: E501
        "_303": "303",  # noqa: E501
        "_304": "304",  # noqa: E501
        "_305": "305",  # noqa: E501
        "_306": "306",  # noqa: E501
        "_307": "307",  # noqa: E501
        "_308": "308",  # noqa: E501
        "_309": "309",  # noqa: E501
        "_310": "310",  # noqa: E501
        "_311": "311",  # noqa: E501
        "_312": "312",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ResponseAggregationsBEGINNTERMIN - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            _0 (ResponseAggregationsBEGINNTERMIN0): [optional]  # noqa: E501
            _1 (ResponseAggregationsBEGINNTERMIN1): [optional]  # noqa: E501
            _2 (ResponseAggregationsBEGINNTERMIN2): [optional]  # noqa: E501
            _101 (ResponseAggregationsBEGINNTERMIN101): [optional]  # noqa: E501
            _102 (ResponseAggregationsBEGINNTERMIN102): [optional]  # noqa: E501
            _103 (ResponseAggregationsBEGINNTERMIN103): [optional]  # noqa: E501
            _104 (ResponseAggregationsBEGINNTERMIN104): [optional]  # noqa: E501
            _105 (ResponseAggregationsBEGINNTERMIN105): [optional]  # noqa: E501
            _106 (ResponseAggregationsBEGINNTERMIN106): [optional]  # noqa: E501
            _107 (ResponseAggregationsBEGINNTERMIN107): [optional]  # noqa: E501
            _108 (ResponseAggregationsBEGINNTERMIN108): [optional]  # noqa: E501
            _109 (ResponseAggregationsBEGINNTERMIN109): [optional]  # noqa: E501
            _110 (ResponseAggregationsBEGINNTERMIN110): [optional]  # noqa: E501
            _111 (ResponseAggregationsBEGINNTERMIN111): [optional]  # noqa: E501
            _112 (ResponseAggregationsBEGINNTERMIN112): [optional]  # noqa: E501
            _113 (ResponseAggregationsBEGINNTERMIN113): [optional]  # noqa: E501
            _201 (ResponseAggregationsBEGINNTERMIN201): [optional]  # noqa: E501
            _202 (ResponseAggregationsBEGINNTERMIN202): [optional]  # noqa: E501
            _203 (ResponseAggregationsBEGINNTERMIN203): [optional]  # noqa: E501
            _204 (ResponseAggregationsBEGINNTERMIN204): [optional]  # noqa: E501
            _205 (ResponseAggregationsBEGINNTERMIN205): [optional]  # noqa: E501
            _206 (ResponseAggregationsBEGINNTERMIN206): [optional]  # noqa: E501
            _207 (ResponseAggregationsBEGINNTERMIN207): [optional]  # noqa: E501
            _208 (ResponseAggregationsBEGINNTERMIN208): [optional]  # noqa: E501
            _209 (ResponseAggregationsBEGINNTERMIN209): [optional]  # noqa: E501
            _210 (ResponseAggregationsBEGINNTERMIN210): [optional]  # noqa: E501
            _211 (ResponseAggregationsBEGINNTERMIN211): [optional]  # noqa: E501
            _212 (ResponseAggregationsBEGINNTERMIN212): [optional]  # noqa: E501
            _301 (ResponseAggregationsBEGINNTERMIN301): [optional]  # noqa: E501
            _302 (ResponseAggregationsBEGINNTERMIN302): [optional]  # noqa: E501
            _303 (ResponseAggregationsBEGINNTERMIN303): [optional]  # noqa: E501
            _304 (ResponseAggregationsBEGINNTERMIN304): [optional]  # noqa: E501
            _305 (ResponseAggregationsBEGINNTERMIN305): [optional]  # noqa: E501
            _306 (ResponseAggregationsBEGINNTERMIN306): [optional]  # noqa: E501
            _307 (ResponseAggregationsBEGINNTERMIN307): [optional]  # noqa: E501
            _308 (ResponseAggregationsBEGINNTERMIN308): [optional]  # noqa: E501
            _309 (ResponseAggregationsBEGINNTERMIN309): [optional]  # noqa: E501
            _310 (ResponseAggregationsBEGINNTERMIN310): [optional]  # noqa: E501
            _311 (ResponseAggregationsBEGINNTERMIN311): [optional]  # noqa: E501
            _312 (ResponseAggregationsBEGINNTERMIN312): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", True)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                        % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ResponseAggregationsBEGINNTERMIN - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            _0 (ResponseAggregationsBEGINNTERMIN0): [optional]  # noqa: E501
            _1 (ResponseAggregationsBEGINNTERMIN1): [optional]  # noqa: E501
            _2 (ResponseAggregationsBEGINNTERMIN2): [optional]  # noqa: E501
            _101 (ResponseAggregationsBEGINNTERMIN101): [optional]  # noqa: E501
            _102 (ResponseAggregationsBEGINNTERMIN102): [optional]  # noqa: E501
            _103 (ResponseAggregationsBEGINNTERMIN103): [optional]  # noqa: E501
            _104 (ResponseAggregationsBEGINNTERMIN104): [optional]  # noqa: E501
            _105 (ResponseAggregationsBEGINNTERMIN105): [optional]  # noqa: E501
            _106 (ResponseAggregationsBEGINNTERMIN106): [optional]  # noqa: E501
            _107 (ResponseAggregationsBEGINNTERMIN107): [optional]  # noqa: E501
            _108 (ResponseAggregationsBEGINNTERMIN108): [optional]  # noqa: E501
            _109 (ResponseAggregationsBEGINNTERMIN109): [optional]  # noqa: E501
            _110 (ResponseAggregationsBEGINNTERMIN110): [optional]  # noqa: E501
            _111 (ResponseAggregationsBEGINNTERMIN111): [optional]  # noqa: E501
            _112 (ResponseAggregationsBEGINNTERMIN112): [optional]  # noqa: E501
            _113 (ResponseAggregationsBEGINNTERMIN113): [optional]  # noqa: E501
            _201 (ResponseAggregationsBEGINNTERMIN201): [optional]  # noqa: E501
            _202 (ResponseAggregationsBEGINNTERMIN202): [optional]  # noqa: E501
            _203 (ResponseAggregationsBEGINNTERMIN203): [optional]  # noqa: E501
            _204 (ResponseAggregationsBEGINNTERMIN204): [optional]  # noqa: E501
            _205 (ResponseAggregationsBEGINNTERMIN205): [optional]  # noqa: E501
            _206 (ResponseAggregationsBEGINNTERMIN206): [optional]  # noqa: E501
            _207 (ResponseAggregationsBEGINNTERMIN207): [optional]  # noqa: E501
            _208 (ResponseAggregationsBEGINNTERMIN208): [optional]  # noqa: E501
            _209 (ResponseAggregationsBEGINNTERMIN209): [optional]  # noqa: E501
            _210 (ResponseAggregationsBEGINNTERMIN210): [optional]  # noqa: E501
            _211 (ResponseAggregationsBEGINNTERMIN211): [optional]  # noqa: E501
            _212 (ResponseAggregationsBEGINNTERMIN212): [optional]  # noqa: E501
            _301 (ResponseAggregationsBEGINNTERMIN301): [optional]  # noqa: E501
            _302 (ResponseAggregationsBEGINNTERMIN302): [optional]  # noqa: E501
            _303 (ResponseAggregationsBEGINNTERMIN303): [optional]  # noqa: E501
            _304 (ResponseAggregationsBEGINNTERMIN304): [optional]  # noqa: E501
            _305 (ResponseAggregationsBEGINNTERMIN305): [optional]  # noqa: E501
            _306 (ResponseAggregationsBEGINNTERMIN306): [optional]  # noqa: E501
            _307 (ResponseAggregationsBEGINNTERMIN307): [optional]  # noqa: E501
            _308 (ResponseAggregationsBEGINNTERMIN308): [optional]  # noqa: E501
            _309 (ResponseAggregationsBEGINNTERMIN309): [optional]  # noqa: E501
            _310 (ResponseAggregationsBEGINNTERMIN310): [optional]  # noqa: E501
            _311 (ResponseAggregationsBEGINNTERMIN311): [optional]  # noqa: E501
            _312 (ResponseAggregationsBEGINNTERMIN312): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                        % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(
                    f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                    f"class with read only attributes."
                )
