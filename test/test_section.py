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

from openapi_client.models.section import Section

class TestSection(unittest.TestCase):
    """Section unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Section:
        """Test Section
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Section`
        """
        model = Section()
        if include_optional:
            return Section(
                id = 'a8b3adb687644b27fafcb3a9875f0f0d_18',
                name = 'Risk factors',
                parent = {"id":"a8b3adb687644b27fafcb3a9875f0f0d_18","name":"Risk factors","parent":null,"index":1,"children":[],"nonPrinting":false},
                index = 1,
                children = [
                    {"id":"a8b3adb687644b27fafcb3a9875f0f0d_18","name":"Risk factors","parent":null,"index":1,"children":[],"nonPrinting":false}
                    ],
                non_printing = True
            )
        else:
            return Section(
        )
        """

    def testSection(self):
        """Test Section"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
