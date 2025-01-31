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

from openapi_client.models.files_list_result import FilesListResult

class TestFilesListResult(unittest.TestCase):
    """FilesListResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FilesListResult:
        """Test FilesListResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FilesListResult`
        """
        model = FilesListResult()
        if include_optional:
            return FilesListResult(
                data = [
                    openapi_client.models.file.File(
                        id = '124efa2a142f472ba1ceab34ed18915f', 
                        name = 'Year-end review', 
                        container = '', 
                        kind = 'Document', 
                        type = '10-K', 
                        template = False, 
                        created = openapi_client.models.action.Action(
                            user = openapi_client.models.user.User(
                                id = 'V1ZVd2VyFzU3NiQ1NDA4NjIzNzk2MjD', 
                                user_name = '', 
                                display_name = '', 
                                first_name = '', 
                                last_name = '', 
                                email = '', ), 
                            date_time = '2019-10-30T15:03:27Z', ), 
                        modified = openapi_client.models.action.Action(
                            date_time = '2019-10-30T15:03:27Z', ), )
                    ],
                next_link = '<opaque_url>'
            )
        else:
            return FilesListResult(
                data = [
                    openapi_client.models.file.File(
                        id = '124efa2a142f472ba1ceab34ed18915f', 
                        name = 'Year-end review', 
                        container = '', 
                        kind = 'Document', 
                        type = '10-K', 
                        template = False, 
                        created = openapi_client.models.action.Action(
                            user = openapi_client.models.user.User(
                                id = 'V1ZVd2VyFzU3NiQ1NDA4NjIzNzk2MjD', 
                                user_name = '', 
                                display_name = '', 
                                first_name = '', 
                                last_name = '', 
                                email = '', ), 
                            date_time = '2019-10-30T15:03:27Z', ), 
                        modified = openapi_client.models.action.Action(
                            date_time = '2019-10-30T15:03:27Z', ), )
                    ],
        )
        """

    def testFilesListResult(self):
        """Test FilesListResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
