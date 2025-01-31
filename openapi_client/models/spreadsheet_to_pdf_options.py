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
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class SpreadsheetToPdfOptions(BaseModel):
    """
    Optional options to export the spreadsheet as a portable document file (.PDF). If no options are provided, all options default to False except:   - `pageHeight`, which defaults to 11   - `pageWidth`, which defaults to 8.5   - `pageOrientation`, which defaults to \"portrait\"   - `pageScale`, which defaults to \"actualSize\"
    """ # noqa: E501
    include_hyperlinks: Optional[StrictBool] = Field(default=False, description="Whether to include hyperlinks when exporting to .PDF. False by default.", alias="includeHyperlinks")
    include_leader_dots: Optional[StrictBool] = Field(default=False, description="Whether to include leader dots when exporting to .PDF. False by default.", alias="includeLeaderDots")
    show_cell_fills: Optional[StrictBool] = Field(default=False, description="Whether to show cell fills when exporting to .PDF. False by default.", alias="showCellFills")
    show_gridlines: Optional[StrictBool] = Field(default=False, description="Whether to show gridlines when exporting to .PDF. False by default.", alias="showGridlines")
    use_cmyk_colorspace: Optional[StrictBool] = Field(default=False, description="Whether to use CMYK colorspace when exporting to .PDF. False by default.", alias="useCmykColorspace")
    include_draft_watermark: Optional[StrictBool] = Field(default=False, description="Whether to include draft watermark when exporting to .PDF. False by default.", alias="includeDraftWatermark")
    include_comments: Optional[StrictBool] = Field(default=False, description="Whether to include comments when exporting to .PDF False by default.", alias="includeComments")
    include_track_changes: Optional[StrictBool] = Field(default=False, description="Whether to include track changes when exporting to .PDF. False by default.", alias="includeTrackChanges")
    only_export_print_areas: Optional[StrictBool] = Field(default=False, description="Whether to only export print areas when exporting to .PDF. False by default.", alias="onlyExportPrintAreas")
    page_height: Optional[Union[Annotated[float, Field(le=100, strict=True, ge=3)], Annotated[int, Field(le=100, strict=True, ge=3)]]] = Field(default=11, description="The height of the exported .PDF, in inches. 11 by default.", alias="pageHeight")
    page_width: Optional[Union[Annotated[float, Field(le=100, strict=True, ge=3)], Annotated[int, Field(le=100, strict=True, ge=3)]]] = Field(default=8.5, description="The width of the exported .PDF, in inches. 8.5 by default.", alias="pageWidth")
    page_orientation: Optional[StrictStr] = Field(default='portrait', description="The orientation of the exported .PDF, such as \"portrait\" or \"landscape\". \"portrait\" by default. ", alias="pageOrientation")
    page_scale: Optional[StrictStr] = Field(default='actualSize', description="The scale of the exported .PDF. \"actualSize\" by default.", alias="pageScale")
    __properties: ClassVar[List[str]] = ["includeHyperlinks", "includeLeaderDots", "showCellFills", "showGridlines", "useCmykColorspace", "includeDraftWatermark", "includeComments", "includeTrackChanges", "onlyExportPrintAreas", "pageHeight", "pageWidth", "pageOrientation", "pageScale"]

    @field_validator('page_orientation')
    def page_orientation_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['portrait', 'landscape']):
            raise ValueError("must be one of enum values ('portrait', 'landscape')")
        return value

    @field_validator('page_scale')
    def page_scale_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['actualSize', 'fitToWidth']):
            raise ValueError("must be one of enum values ('actualSize', 'fitToWidth')")
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
        """Create an instance of SpreadsheetToPdfOptions from a JSON string"""
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
        """Create an instance of SpreadsheetToPdfOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "includeHyperlinks": obj.get("includeHyperlinks") if obj.get("includeHyperlinks") is not None else False,
            "includeLeaderDots": obj.get("includeLeaderDots") if obj.get("includeLeaderDots") is not None else False,
            "showCellFills": obj.get("showCellFills") if obj.get("showCellFills") is not None else False,
            "showGridlines": obj.get("showGridlines") if obj.get("showGridlines") is not None else False,
            "useCmykColorspace": obj.get("useCmykColorspace") if obj.get("useCmykColorspace") is not None else False,
            "includeDraftWatermark": obj.get("includeDraftWatermark") if obj.get("includeDraftWatermark") is not None else False,
            "includeComments": obj.get("includeComments") if obj.get("includeComments") is not None else False,
            "includeTrackChanges": obj.get("includeTrackChanges") if obj.get("includeTrackChanges") is not None else False,
            "onlyExportPrintAreas": obj.get("onlyExportPrintAreas") if obj.get("onlyExportPrintAreas") is not None else False,
            "pageHeight": obj.get("pageHeight") if obj.get("pageHeight") is not None else 11,
            "pageWidth": obj.get("pageWidth") if obj.get("pageWidth") is not None else 8.5,
            "pageOrientation": obj.get("pageOrientation") if obj.get("pageOrientation") is not None else 'portrait',
            "pageScale": obj.get("pageScale") if obj.get("pageScale") is not None else 'actualSize'
        })
        return _obj


