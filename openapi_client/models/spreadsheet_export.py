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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.spreadsheet_to_csv_options import SpreadsheetToCsvOptions
from openapi_client.models.spreadsheet_to_pdf_options import SpreadsheetToPdfOptions
from openapi_client.models.spreadsheet_to_xlsx_options import SpreadsheetToXlsxOptions
from typing import Optional, Set
from typing_extensions import Self

class SpreadsheetExport(BaseModel):
    """
    Details about a spreadsheet export.
    """ # noqa: E501
    format: StrictStr = Field(description="The file format to export the spreadsheet as.")
    sheets: Optional[List[StrictStr]] = Field(default=None, description="The IDs of the sheets within the spreadsheet to export. Omit to export the entire spreadsheet.  Note: When exporting to .CSV, you can export only the entire spreadsheet or a single sheet. When exporting the entire spreadsheet, the resulting file is a .ZIP of .CSV files, with one .CSV file per sheet.")
    xlsx_options: Optional[SpreadsheetToXlsxOptions] = Field(default=None, alias="xlsxOptions")
    pdf_options: Optional[SpreadsheetToPdfOptions] = Field(default=None, alias="pdfOptions")
    csv_options: Optional[SpreadsheetToCsvOptions] = Field(default=None, alias="csvOptions")
    __properties: ClassVar[List[str]] = ["format", "sheets", "xlsxOptions", "pdfOptions", "csvOptions"]

    @field_validator('format')
    def format_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['pdf', 'xlsx', 'csv']):
            raise ValueError("must be one of enum values ('pdf', 'xlsx', 'csv')")
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
        """Create an instance of SpreadsheetExport from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of xlsx_options
        if self.xlsx_options:
            _dict['xlsxOptions'] = self.xlsx_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pdf_options
        if self.pdf_options:
            _dict['pdfOptions'] = self.pdf_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of csv_options
        if self.csv_options:
            _dict['csvOptions'] = self.csv_options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SpreadsheetExport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "format": obj.get("format"),
            "sheets": obj.get("sheets"),
            "xlsxOptions": SpreadsheetToXlsxOptions.from_dict(obj["xlsxOptions"]) if obj.get("xlsxOptions") is not None else None,
            "pdfOptions": SpreadsheetToPdfOptions.from_dict(obj["pdfOptions"]) if obj.get("pdfOptions") is not None else None,
            "csvOptions": SpreadsheetToCsvOptions.from_dict(obj["csvOptions"]) if obj.get("csvOptions") is not None else None
        })
        return _obj


