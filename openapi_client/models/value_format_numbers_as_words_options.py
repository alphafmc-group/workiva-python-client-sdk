# coding: utf-8

"""
    Platform API

    Use the Workiva Platform API to programmatically manage items in the Workiva platform, such as files, folders, tasks, comments, documents, spreadsheets, and presentations. 

    The version of the OpenAPI document: v1
    Contact: platformsupport@workiva.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ValueFormatNumbersAsWordsOptions(BaseModel):
    """
    Options relevant when showing numbers as words. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT. In order for these options to take effect showNumbersAsWords must be set to true. 
    """ # noqa: E501
    capitalize_first_word: Optional[StrictBool] = Field(default=False, description="Capitalize the first word. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT.", alias="capitalizeFirstWord")
    display_zero_as: Optional[StrictStr] = Field(default='ZERO', description="The word to use for zero. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT.", alias="displayZeroAs")
    __properties: ClassVar[List[str]] = ["capitalizeFirstWord", "displayZeroAs"]

    @field_validator('display_zero_as')
    def display_zero_as_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ZERO', 'NO', 'NONE', 'NOTHING', 'NIL', 'NOT', 'NOMINAL', 'IMMATERIAL']):
            raise ValueError("must be one of enum values ('ZERO', 'NO', 'NONE', 'NOTHING', 'NIL', 'NOT', 'NOMINAL', 'IMMATERIAL')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ValueFormatNumbersAsWordsOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ValueFormatNumbersAsWordsOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "capitalizeFirstWord": obj.get("capitalizeFirstWord") if obj.get("capitalizeFirstWord") is not None else False,
            "displayZeroAs": obj.get("displayZeroAs") if obj.get("displayZeroAs") is not None else 'ZERO'
        })
        return _obj


