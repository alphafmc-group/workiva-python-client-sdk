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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SectionCopy(BaseModel):
    """
    Details about the destination document and, optionally, the destination section.
    """ # noqa: E501
    document: StrictStr = Field(description="The unique identifier of the document to copy a section into")
    section_index: Optional[StrictInt] = Field(default=None, description="The integer index of where within the siblings to place the new section; 0 by default. To place the section at the end of its siblings, use the special value -1.", alias="sectionIndex")
    section_parent: Optional[StrictStr] = Field(default=None, description="The ID of the parent section to copy the section into. To place the section at the top level of the document, use the default null.", alias="sectionParent")
    section_name: Optional[StrictStr] = Field(default=None, description="The name of the new section, if different than the source section", alias="sectionName")
    __properties: ClassVar[List[str]] = ["document", "sectionIndex", "sectionParent", "sectionName"]

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
        """Create an instance of SectionCopy from a JSON string"""
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
        # set to None if section_parent (nullable) is None
        # and model_fields_set contains the field
        if self.section_parent is None and "section_parent" in self.model_fields_set:
            _dict['sectionParent'] = None

        # set to None if section_name (nullable) is None
        # and model_fields_set contains the field
        if self.section_name is None and "section_name" in self.model_fields_set:
            _dict['sectionName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SectionCopy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "document": obj.get("document"),
            "sectionIndex": obj.get("sectionIndex"),
            "sectionParent": obj.get("sectionParent"),
            "sectionName": obj.get("sectionName")
        })
        return _obj


