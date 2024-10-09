# coding: utf-8

"""
    Platform API

    Use the Workiva Platform API to programmatically manage items in the Workiva platform, such as files, folders, tasks, comments, documents, spreadsheets, and presentations. 

    The version of the OpenAPI document: v1
    Contact: platformsupport@workiva.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.cell_data import CellData

class TestCellData(unittest.TestCase):
    """CellData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CellData:
        """Test CellData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CellData`
        """
        model = CellData()
        if include_optional:
            return CellData(
                value = None,
                calculated_value = None,
                formats = openapi_client.models.formats.Formats(
                    text_format = openapi_client.models.text_format.TextFormat(
                        bold = True, 
                        italic = True, 
                        underline = True, 
                        strikethrough = True, 
                        font_family = 'Times New Roman', 
                        font_size = 12, 
                        font_color = '#000000', ), 
                    value_format = openapi_client.models.value_format.ValueFormat(
                        value_format_type = 'AUTOMATIC', 
                        entered_in = 'MILLIONTHS', 
                        shown_in = 'MILLIONTHS', 
                        precision = openapi_client.models.value_format_precision.ValueFormat_precision(
                            auto = True, 
                            value = -15, ), 
                        show_currency_symbol = True, 
                        currency_symbol = openapi_client.models.value_format_currency_symbol.ValueFormat_currencySymbol(
                            generic = 'DOLLAR', 
                            currency = openapi_client.models.value_format_currency_symbol_currency.ValueFormat_currencySymbol_currency(
                                code = 'AUD', 
                                display = 'SYMBOL', ), ), 
                        percent_symbol = 'NONE', 
                        symbol_align = 'SYMBOL DEFAULT', 
                        show_leading_zero = True, 
                        show_thousands_separator = True, 
                        use_parens_for_negatives = True, 
                        show_numbers_as_words = True, 
                        display_zero_as = 'ZERO', 
                        numbers_as_words_options = openapi_client.models.value_format_numbers_as_words_options.ValueFormat_numbersAsWordsOptions(
                            capitalize_first_word = True, 
                            display_zero_as = 'ZERO', ), 
                        show_sign_rounded_zero = True, 
                        show_positive_sign = True, 
                        date_uppercase_all = True, 
                        date_abbreviate_month = True, 
                        date_format_string = 'd/m/yyyy', 
                        period_format = openapi_client.models.value_format_period_format.ValueFormat_periodFormat(
                            display = 'RAW', 
                            separator = 'COMMA', 
                            show_labels = True, 
                            show_numbers_as_words = True, 
                            capitalize_first_word = True, ), 
                        prefix = '', 
                        suffix = '', ), 
                    cell_format = openapi_client.models.cell_format.CellFormat(
                        indent = openapi_client.models.cell_format_indent.CellFormat_indent(
                            value = 0, 
                            unit = 'INCHES', ), 
                        horizontal_align = 'LEFT', 
                        vertical_align = 'TOP', 
                        text_rotation = 'HORIZONTAL', 
                        background_color = '#000000', 
                        leader_dots = 'NARROW', 
                        borders = openapi_client.models.cell_format_borders.CellFormat_borders(
                            top = {"style":"SINGLE","weight":2,"color":"#000000"}, 
                            bottom = {"style":"SINGLE","weight":2,"color":"#000000"}, 
                            left = {"style":"SINGLE","weight":2,"color":"#000000"}, 
                            right = {"style":"SINGLE","weight":2,"color":"#000000"}, ), ), ),
                effective_formats = openapi_client.models.effective_formats.EffectiveFormats(
                    text_format = openapi_client.models.text_format.TextFormat(
                        bold = True, 
                        italic = True, 
                        underline = True, 
                        strikethrough = True, 
                        font_family = 'Times New Roman', 
                        font_size = 12, 
                        font_color = '#000000', ), 
                    value_format = openapi_client.models.value_format.ValueFormat(
                        value_format_type = 'AUTOMATIC', 
                        entered_in = 'MILLIONTHS', 
                        shown_in = 'MILLIONTHS', 
                        precision = openapi_client.models.value_format_precision.ValueFormat_precision(
                            auto = True, 
                            value = -15, ), 
                        show_currency_symbol = True, 
                        currency_symbol = openapi_client.models.value_format_currency_symbol.ValueFormat_currencySymbol(
                            generic = 'DOLLAR', 
                            currency = openapi_client.models.value_format_currency_symbol_currency.ValueFormat_currencySymbol_currency(
                                code = 'AUD', 
                                display = 'SYMBOL', ), ), 
                        percent_symbol = 'NONE', 
                        symbol_align = 'SYMBOL DEFAULT', 
                        show_leading_zero = True, 
                        show_thousands_separator = True, 
                        use_parens_for_negatives = True, 
                        show_numbers_as_words = True, 
                        display_zero_as = 'ZERO', 
                        numbers_as_words_options = openapi_client.models.value_format_numbers_as_words_options.ValueFormat_numbersAsWordsOptions(
                            capitalize_first_word = True, 
                            display_zero_as = 'ZERO', ), 
                        show_sign_rounded_zero = True, 
                        show_positive_sign = True, 
                        date_uppercase_all = True, 
                        date_abbreviate_month = True, 
                        date_format_string = 'd/m/yyyy', 
                        period_format = openapi_client.models.value_format_period_format.ValueFormat_periodFormat(
                            display = 'RAW', 
                            separator = 'COMMA', 
                            show_labels = True, 
                            show_numbers_as_words = True, 
                            capitalize_first_word = True, ), 
                        prefix = '', 
                        suffix = '', ), 
                    cell_format = openapi_client.models.cell_format.CellFormat(
                        indent = openapi_client.models.cell_format_indent.CellFormat_indent(
                            value = 0, 
                            unit = 'INCHES', ), 
                        horizontal_align = 'LEFT', 
                        vertical_align = 'TOP', 
                        text_rotation = 'HORIZONTAL', 
                        background_color = '#000000', 
                        leader_dots = 'NARROW', 
                        borders = openapi_client.models.cell_format_borders.CellFormat_borders(
                            top = {"style":"SINGLE","weight":2,"color":"#000000"}, 
                            bottom = {"style":"SINGLE","weight":2,"color":"#000000"}, 
                            left = {"style":"SINGLE","weight":2,"color":"#000000"}, 
                            right = {"style":"SINGLE","weight":2,"color":"#000000"}, ), ), )
            )
        else:
            return CellData(
        )
        """

    def testCellData(self):
        """Test CellData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
