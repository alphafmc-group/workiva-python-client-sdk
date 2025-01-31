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

from openapi_client.models.spreadsheet_to_pdf_options import SpreadsheetToPdfOptions

class TestSpreadsheetToPdfOptions(unittest.TestCase):
    """SpreadsheetToPdfOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SpreadsheetToPdfOptions:
        """Test SpreadsheetToPdfOptions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpreadsheetToPdfOptions`
        """
        model = SpreadsheetToPdfOptions()
        if include_optional:
            return SpreadsheetToPdfOptions(
                include_hyperlinks = True,
                include_leader_dots = True,
                show_cell_fills = True,
                show_gridlines = True,
                use_cmyk_colorspace = True,
                include_draft_watermark = True,
                include_comments = True,
                include_track_changes = True,
                only_export_print_areas = True,
                page_height = 14,
                page_width = 11,
                page_orientation = 'portrait',
                page_scale = 'actualSize'
            )
        else:
            return SpreadsheetToPdfOptions(
        )
        """

    def testSpreadsheetToPdfOptions(self):
        """Test SpreadsheetToPdfOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
