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

from openapi_client.models.sheet_update_resize_columns_to_fit import SheetUpdateResizeColumnsToFit

class TestSheetUpdateResizeColumnsToFit(unittest.TestCase):
    """SheetUpdateResizeColumnsToFit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SheetUpdateResizeColumnsToFit:
        """Test SheetUpdateResizeColumnsToFit
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SheetUpdateResizeColumnsToFit`
        """
        model = SheetUpdateResizeColumnsToFit()
        if include_optional:
            return SheetUpdateResizeColumnsToFit(
                intervals = [
                    openapi_client.models.interval.Interval(
                        start = 0, 
                        end = 0, )
                    ]
            )
        else:
            return SheetUpdateResizeColumnsToFit(
                intervals = [
                    openapi_client.models.interval.Interval(
                        start = 0, 
                        end = 0, )
                    ],
        )
        """

    def testSheetUpdateResizeColumnsToFit(self):
        """Test SheetUpdateResizeColumnsToFit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
