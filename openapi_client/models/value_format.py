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
from typing_extensions import Annotated
from openapi_client.models.value_format_currency_symbol import ValueFormatCurrencySymbol
from openapi_client.models.value_format_numbers_as_words_options import ValueFormatNumbersAsWordsOptions
from openapi_client.models.value_format_period_format import ValueFormatPeriodFormat
from openapi_client.models.value_format_precision import ValueFormatPrecision
from typing import Optional, Set
from typing_extensions import Self

class ValueFormat(BaseModel):
    """
    Value Formats. Fields that are omitted will be ignored.
    """ # noqa: E501
    value_format_type: Optional[StrictStr] = Field(default=None, description="The value format type of the content. Setting this property will clear any other ValueFormat properties that are not valid for the new value format type.", alias="valueFormatType")
    entered_in: Optional[StrictStr] = Field(default=None, description="The scale cell values are entered in. Valid for AUTOMATIC, ACCOUNTING, CURRENCY, and NUMBER.", alias="enteredIn")
    shown_in: Optional[StrictStr] = Field(default=None, description="The scale cell values are displayed in. Valid for AUTOMATIC, ACCOUNTING, CURRENCY, and NUMBER.", alias="shownIn")
    precision: Optional[ValueFormatPrecision] = None
    show_currency_symbol: Optional[StrictBool] = Field(default=None, description="Render numbers with a currency symbol. Valid for ACCOUNTING and CURRENCY.", alias="showCurrencySymbol")
    currency_symbol: Optional[ValueFormatCurrencySymbol] = Field(default=None, alias="currencySymbol")
    percent_symbol: Optional[StrictStr] = Field(default=None, description="Render numbers with a percent symbol. Valid for PERCENT.", alias="percentSymbol")
    symbol_align: Optional[StrictStr] = Field(default=None, description="Where to render the symbol relative to the value. All values valid for ACCOUNTING and CURRENCY. Left values valid for NUMBER. Right values valid for PERCENT.", alias="symbolAlign")
    show_leading_zero: Optional[StrictBool] = Field(default=None, description="Include a leading zero for decimal numbers with no whole number part. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT.", alias="showLeadingZero")
    show_thousands_separator: Optional[StrictBool] = Field(default=None, description="Render the thousands separator. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT.", alias="showThousandsSeparator")
    use_parens_for_negatives: Optional[StrictBool] = Field(default=None, description="Render parentheses around the number instead of a negative symbol. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT.", alias="useParensForNegatives")
    show_numbers_as_words: Optional[StrictBool] = Field(default=None, description="Render the number as words instead of digits. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT.", alias="showNumbersAsWords")
    display_zero_as: Optional[StrictStr] = Field(default=None, description="The symbol to use for zero. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT. This field controls the symbol to use for zero when not using showNumbersAsWords. ", alias="displayZeroAs")
    numbers_as_words_options: Optional[ValueFormatNumbersAsWordsOptions] = Field(default=None, alias="numbersAsWordsOptions")
    show_sign_rounded_zero: Optional[StrictBool] = Field(default=None, description="Render the sign on values rounded to zero. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT.", alias="showSignRoundedZero")
    show_positive_sign: Optional[StrictBool] = Field(default=None, description="Render the positive sign on numbers greater than zero. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT.", alias="showPositiveSign")
    date_uppercase_all: Optional[StrictBool] = Field(default=None, description="Uppercase all characters in the date string. Valid for DATE.", alias="dateUppercaseAll")
    date_abbreviate_month: Optional[StrictBool] = Field(default=None, description="Use month abbreviations instead of full month names. Valid for DATE.", alias="dateAbbreviateMonth")
    date_format_string: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Format to use when rendering the date. Valid for DATE.", alias="dateFormatString")
    period_format: Optional[ValueFormatPeriodFormat] = Field(default=None, alias="periodFormat")
    prefix: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Custom prefix value to render in the cell. Valid for ACCOUNTING, CURRENCY, NUMBER, PERCENT, and DATE.")
    suffix: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="Custom suffix value to render in the cell. Valid for ACCOUNTING, CURRENCY, NUMBER, PERCENT, and DATE.")
    __properties: ClassVar[List[str]] = ["valueFormatType", "enteredIn", "shownIn", "precision", "showCurrencySymbol", "currencySymbol", "percentSymbol", "symbolAlign", "showLeadingZero", "showThousandsSeparator", "useParensForNegatives", "showNumbersAsWords", "displayZeroAs", "numbersAsWordsOptions", "showSignRoundedZero", "showPositiveSign", "dateUppercaseAll", "dateAbbreviateMonth", "dateFormatString", "periodFormat", "prefix", "suffix"]

    @field_validator('value_format_type')
    def value_format_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AUTOMATIC', 'AUTOMATIC ACCOUNTING', 'AUTOMATIC CURRENCY', 'AUTOMATIC NUMBER', 'AUTOMATIC PERCENT', 'AUTOMATIC DATE', 'AUTOMATIC PERIOD', 'AUTOMATIC TEXT', 'ACCOUNTING', 'CURRENCY', 'NUMBER', 'PERCENT', 'DATE', 'PERIOD', 'TEXT']):
            raise ValueError("must be one of enum values ('AUTOMATIC', 'AUTOMATIC ACCOUNTING', 'AUTOMATIC CURRENCY', 'AUTOMATIC NUMBER', 'AUTOMATIC PERCENT', 'AUTOMATIC DATE', 'AUTOMATIC PERIOD', 'AUTOMATIC TEXT', 'ACCOUNTING', 'CURRENCY', 'NUMBER', 'PERCENT', 'DATE', 'PERIOD', 'TEXT')")
        return value

    @field_validator('entered_in')
    def entered_in_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MILLIONTHS', 'BASIS POINTS', 'THOUSANDTHS', 'HUNDREDTHS', 'ONES', 'THOUSANDS', 'TEN THOUSANDS', 'MILLIONS', 'HUNDRED MILLIONS', 'BILLIONS', 'TRILLIONS']):
            raise ValueError("must be one of enum values ('MILLIONTHS', 'BASIS POINTS', 'THOUSANDTHS', 'HUNDREDTHS', 'ONES', 'THOUSANDS', 'TEN THOUSANDS', 'MILLIONS', 'HUNDRED MILLIONS', 'BILLIONS', 'TRILLIONS')")
        return value

    @field_validator('shown_in')
    def shown_in_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MILLIONTHS', 'BASIS POINTS', 'THOUSANDTHS', 'HUNDREDTHS', 'ONES', 'THOUSANDS', 'TEN THOUSANDS', 'MILLIONS', 'HUNDRED MILLIONS', 'BILLIONS', 'TRILLIONS']):
            raise ValueError("must be one of enum values ('MILLIONTHS', 'BASIS POINTS', 'THOUSANDTHS', 'HUNDREDTHS', 'ONES', 'THOUSANDS', 'TEN THOUSANDS', 'MILLIONS', 'HUNDRED MILLIONS', 'BILLIONS', 'TRILLIONS')")
        return value

    @field_validator('percent_symbol')
    def percent_symbol_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NONE', 'SYMBOL', 'WORD']):
            raise ValueError("must be one of enum values ('NONE', 'SYMBOL', 'WORD')")
        return value

    @field_validator('symbol_align')
    def symbol_align_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SYMBOL DEFAULT', 'LEFT', 'LEFT INSIDE', 'RIGHT', 'RIGHT INSIDE', 'RIGHT SPACED INSIDE', 'RIGHT SPACED']):
            raise ValueError("must be one of enum values ('SYMBOL DEFAULT', 'LEFT', 'LEFT INSIDE', 'RIGHT', 'RIGHT INSIDE', 'RIGHT SPACED INSIDE', 'RIGHT SPACED')")
        return value

    @field_validator('display_zero_as')
    def display_zero_as_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ZERO', 'EM DASH', 'EN DASH', 'HYPHEN', 'BLANK']):
            raise ValueError("must be one of enum values ('ZERO', 'EM DASH', 'EN DASH', 'HYPHEN', 'BLANK')")
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
        """Create an instance of ValueFormat from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of precision
        if self.precision:
            _dict['precision'] = self.precision.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency_symbol
        if self.currency_symbol:
            _dict['currencySymbol'] = self.currency_symbol.to_dict()
        # override the default output from pydantic by calling `to_dict()` of numbers_as_words_options
        if self.numbers_as_words_options:
            _dict['numbersAsWordsOptions'] = self.numbers_as_words_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of period_format
        if self.period_format:
            _dict['periodFormat'] = self.period_format.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ValueFormat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "valueFormatType": obj.get("valueFormatType"),
            "enteredIn": obj.get("enteredIn"),
            "shownIn": obj.get("shownIn"),
            "precision": ValueFormatPrecision.from_dict(obj["precision"]) if obj.get("precision") is not None else None,
            "showCurrencySymbol": obj.get("showCurrencySymbol"),
            "currencySymbol": ValueFormatCurrencySymbol.from_dict(obj["currencySymbol"]) if obj.get("currencySymbol") is not None else None,
            "percentSymbol": obj.get("percentSymbol"),
            "symbolAlign": obj.get("symbolAlign"),
            "showLeadingZero": obj.get("showLeadingZero"),
            "showThousandsSeparator": obj.get("showThousandsSeparator"),
            "useParensForNegatives": obj.get("useParensForNegatives"),
            "showNumbersAsWords": obj.get("showNumbersAsWords"),
            "displayZeroAs": obj.get("displayZeroAs"),
            "numbersAsWordsOptions": ValueFormatNumbersAsWordsOptions.from_dict(obj["numbersAsWordsOptions"]) if obj.get("numbersAsWordsOptions") is not None else None,
            "showSignRoundedZero": obj.get("showSignRoundedZero"),
            "showPositiveSign": obj.get("showPositiveSign"),
            "dateUppercaseAll": obj.get("dateUppercaseAll"),
            "dateAbbreviateMonth": obj.get("dateAbbreviateMonth"),
            "dateFormatString": obj.get("dateFormatString"),
            "periodFormat": ValueFormatPeriodFormat.from_dict(obj["periodFormat"]) if obj.get("periodFormat") is not None else None,
            "prefix": obj.get("prefix"),
            "suffix": obj.get("suffix")
        })
        return _obj


