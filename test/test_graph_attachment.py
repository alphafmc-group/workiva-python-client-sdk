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

from openapi_client.models.graph_attachment import GraphAttachment

class TestGraphAttachment(unittest.TestCase):
    """GraphAttachment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GraphAttachment:
        """Test GraphAttachment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GraphAttachment`
        """
        model = GraphAttachment()
        if include_optional:
            return GraphAttachment(
                id = '0a0da34f-bf3e-47fc-bc47-946ab14900b7',
                file_name = 'signature.jpg'
            )
        else:
            return GraphAttachment(
        )
        """

    def testGraphAttachment(self):
        """Test GraphAttachment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
