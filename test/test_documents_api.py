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

from openapi_client.api.documents_api import DocumentsApi


class TestDocumentsApi(unittest.TestCase):
    """DocumentsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DocumentsApi()

    def tearDown(self) -> None:
        pass

    def test_copy_section(self) -> None:
        """Test case for copy_section

        Copy section
        """
        pass

    def test_create_section(self) -> None:
        """Test case for create_section

        Create a new section in a document
        """
        pass

    def test_delete_section_by_id(self) -> None:
        """Test case for delete_section_by_id

        Delete a single section
        """
        pass

    def test_document_export(self) -> None:
        """Test case for document_export

        Initiate a document export
        """
        pass

    def test_get_document_by_id(self) -> None:
        """Test case for get_document_by_id

        Retrieve a single document
        """
        pass

    def test_get_documents(self) -> None:
        """Test case for get_documents

        Retrieve a list of documents
        """
        pass

    def test_get_section_by_id(self) -> None:
        """Test case for get_section_by_id

        Retrieve a single section
        """
        pass

    def test_get_sections(self) -> None:
        """Test case for get_sections

        Retrieve a list of sections
        """
        pass

    def test_partially_update_section_by_id(self) -> None:
        """Test case for partially_update_section_by_id

        Partially update a single section
        """
        pass

    def test_update_section_by_id(self) -> None:
        """Test case for update_section_by_id

        Update a single section
        """
        pass


if __name__ == '__main__':
    unittest.main()
