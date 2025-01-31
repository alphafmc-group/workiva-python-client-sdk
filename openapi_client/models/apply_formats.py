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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.cell_format import CellFormat
from openapi_client.models.range import Range
from openapi_client.models.text_format import TextFormat
from openapi_client.models.value_format import ValueFormat
from typing import Optional, Set
from typing_extensions import Self

class ApplyFormats(BaseModel):
    """
    Apply formats to a list of ranges
    """ # noqa: E501
    ranges: List[Range] = Field(description="The ranges to format")
    text_format: Optional[TextFormat] = Field(default=None, alias="textFormat")
    value_format: Optional[ValueFormat] = Field(default=None, alias="valueFormat")
    cell_format: Optional[CellFormat] = Field(default=None, alias="cellFormat")
    __properties: ClassVar[List[str]] = ["ranges", "textFormat", "valueFormat", "cellFormat"]

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
        """Create an instance of ApplyFormats from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in ranges (list)
        _items = []
        if self.ranges:
            for _item_ranges in self.ranges:
                if _item_ranges:
                    _items.append(_item_ranges.to_dict())
            _dict['ranges'] = _items
        # override the default output from pydantic by calling `to_dict()` of text_format
        if self.text_format:
            _dict['textFormat'] = self.text_format.to_dict()
        # override the default output from pydantic by calling `to_dict()` of value_format
        if self.value_format:
            _dict['valueFormat'] = self.value_format.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cell_format
        if self.cell_format:
            _dict['cellFormat'] = self.cell_format.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplyFormats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ranges": [Range.from_dict(_item) for _item in obj["ranges"]] if obj.get("ranges") is not None else None,
            "textFormat": TextFormat.from_dict(obj["textFormat"]) if obj.get("textFormat") is not None else None,
            "valueFormat": ValueFormat.from_dict(obj["valueFormat"]) if obj.get("valueFormat") is not None else None,
            "cellFormat": CellFormat.from_dict(obj["cellFormat"]) if obj.get("cellFormat") is not None else None
        })
        return _obj


