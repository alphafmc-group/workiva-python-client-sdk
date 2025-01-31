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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.graph_attachment import GraphAttachment
from openapi_client.models.matrix_column import MatrixColumn
from openapi_client.models.matrix_sample import MatrixSample
from typing import Optional, Set
from typing_extensions import Self

class Matrix(BaseModel):
    """
    Details about a matrix, including its name and ID.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the matrix")
    name: Optional[StrictStr] = Field(default=None, description="The name of the matrix")
    data_columns: Optional[List[MatrixColumn]] = Field(default=None, description="An array of the data columns in the matrix", alias="dataColumns")
    result_columns: Optional[List[MatrixColumn]] = Field(default=None, description="An array of the result columns in the matrix", alias="resultColumns")
    samples: Optional[List[MatrixSample]] = Field(default=None, description="An optional array of partial information about the samples on the matrix. To include in the response, provide the query parameter `$expand=samples`. To include the samples' attachments, provide the parameter `$expand=samples,samples.attachments`.")
    attachments: Optional[List[GraphAttachment]] = Field(default=None, description="An optional array of partial information about the attachments on the matrix. To include in the response, provide the query string `$expand=attachments`.")
    __properties: ClassVar[List[str]] = ["id", "name", "dataColumns", "resultColumns", "samples", "attachments"]

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
        """Create an instance of Matrix from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "samples",
            "attachments",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in data_columns (list)
        _items = []
        if self.data_columns:
            for _item_data_columns in self.data_columns:
                if _item_data_columns:
                    _items.append(_item_data_columns.to_dict())
            _dict['dataColumns'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in result_columns (list)
        _items = []
        if self.result_columns:
            for _item_result_columns in self.result_columns:
                if _item_result_columns:
                    _items.append(_item_result_columns.to_dict())
            _dict['resultColumns'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in samples (list)
        _items = []
        if self.samples:
            for _item_samples in self.samples:
                if _item_samples:
                    _items.append(_item_samples.to_dict())
            _dict['samples'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Matrix from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "dataColumns": [MatrixColumn.from_dict(_item) for _item in obj["dataColumns"]] if obj.get("dataColumns") is not None else None,
            "resultColumns": [MatrixColumn.from_dict(_item) for _item in obj["resultColumns"]] if obj.get("resultColumns") is not None else None,
            "samples": [MatrixSample.from_dict(_item) for _item in obj["samples"]] if obj.get("samples") is not None else None,
            "attachments": [GraphAttachment.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None
        })
        return _obj


