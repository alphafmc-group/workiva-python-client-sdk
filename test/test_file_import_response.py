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

from openapi_client.models.file_import_response import FileImportResponse

class TestFileImportResponse(unittest.TestCase):
    """FileImportResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FileImportResponse:
        """Test FileImportResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FileImportResponse`
        """
        model = FileImportResponse()
        if include_optional:
            return FileImportResponse(
                upload_url = '<opaque_url>'
            )
        else:
            return FileImportResponse(
        )
        """

    def testFileImportResponse(self):
        """Test FileImportResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
