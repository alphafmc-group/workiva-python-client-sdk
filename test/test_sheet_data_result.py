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

from openapi_client.models.sheet_data_result import SheetDataResult

class TestSheetDataResult(unittest.TestCase):
    """SheetDataResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SheetDataResult:
        """Test SheetDataResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SheetDataResult`
        """
        model = SheetDataResult()
        if include_optional:
            return SheetDataResult(
                data = {"cells":[[{"calculatedValue":2,"effectiveFormats":{"cellFormat":{"backgroundColor":"#d0e8ff","borders":{"bottom":{"color":"#000","style":"SINGLE","weight":1},"left":{"color":"#000","style":"SINGLE","weight":1},"right":null,"top":{"color":"#000","style":"SINGLE","weight":1}},"horizontalAlign":"RIGHT","indent":{"unit":"INCHES","value":0},"leaderDots":null,"textRotation":null,"verticalAlign":"BOTTOM"},"textFormat":{"bold":true,"fontColor":"#000000","fontFamily":"Arial","fontSize":10,"italic":false,"strikethrough":false,"underline":false},"valueFormat":{"currencySymbol":{"currency":{"code":"EUR","display":"SYMBOL"},"generic":null},"dateAbbreviateMonth":null,"dateFormatString":null,"dateUppercaseAll":null,"displayZeroAs":"ZERO","enteredIn":"ONES","numbersAsWordsOptions":{"capitalizeFirstWord":false,"displayZeroAs":null},"percentSymbol":null,"periodFormat":null,"precision":{"auto":false,"value":2},"prefix":"","showCurrencySymbol":true,"showLeadingZero":true,"showNumbersAsWords":false,"showPositiveSign":false,"showSignRoundedZero":false,"showThousandsSeparator":true,"shownIn":"ONES","suffix":"","symbolAlign":"SYMBOL DEFAULT","useParensForNegatives":false,"valueFormatType":"CURRENCY"}},"formats":{"cellFormat":{"backgroundColor":"#d0e8ff","borders":{"bottom":{"color":"#000","style":"SINGLE","weight":1},"left":{"color":"#000","style":"SINGLE","weight":1},"right":null,"top":{"color":"#000","style":"SINGLE","weight":1}},"horizontalAlign":null,"indent":null,"leaderDots":null,"textRotation":null,"verticalAlign":null},"textFormat":{"bold":true,"fontColor":null,"fontFamily":null,"fontSize":null,"italic":null,"strikethrough":null,"underline":null},"valueFormat":{"currencySymbol":{"currency":{"code":"EUR","display":"SYMBOL"},"generic":null},"dateAbbreviateMonth":null,"dateFormatString":null,"dateUppercaseAll":null,"displayZeroAs":"ZERO","enteredIn":"ONES","numbersAsWordsOptions":{"capitalizeFirstWord":false,"displayZeroAs":null},"percentSymbol":null,"periodFormat":null,"precision":{"auto":false,"value":2},"prefix":"","showCurrencySymbol":true,"showLeadingZero":true,"showNumbersAsWords":false,"showPositiveSign":null,"showSignRoundedZero":false,"showThousandsSeparator":true,"shownIn":"ONES","suffix":"","symbolAlign":null,"useParensForNegatives":false,"valueFormatType":"CURRENCY"}},"value":"=1+1"}]],"columnMetadata":[{"hidden":false,"size":75}],"merges":[{"startColumn":0,"startRow":0,"stopColumn":1,"stopRow":0}],"range":{"startColumn":0,"startRow":0,"stopColumn":0,"stopRow":0},"rowMetadata":[{"filtered":false,"hidden":false,"size":16}]},
                next_link = '<opaque_url>'
            )
        else:
            return SheetDataResult(
                data = {"cells":[[{"calculatedValue":2,"effectiveFormats":{"cellFormat":{"backgroundColor":"#d0e8ff","borders":{"bottom":{"color":"#000","style":"SINGLE","weight":1},"left":{"color":"#000","style":"SINGLE","weight":1},"right":null,"top":{"color":"#000","style":"SINGLE","weight":1}},"horizontalAlign":"RIGHT","indent":{"unit":"INCHES","value":0},"leaderDots":null,"textRotation":null,"verticalAlign":"BOTTOM"},"textFormat":{"bold":true,"fontColor":"#000000","fontFamily":"Arial","fontSize":10,"italic":false,"strikethrough":false,"underline":false},"valueFormat":{"currencySymbol":{"currency":{"code":"EUR","display":"SYMBOL"},"generic":null},"dateAbbreviateMonth":null,"dateFormatString":null,"dateUppercaseAll":null,"displayZeroAs":"ZERO","enteredIn":"ONES","numbersAsWordsOptions":{"capitalizeFirstWord":false,"displayZeroAs":null},"percentSymbol":null,"periodFormat":null,"precision":{"auto":false,"value":2},"prefix":"","showCurrencySymbol":true,"showLeadingZero":true,"showNumbersAsWords":false,"showPositiveSign":false,"showSignRoundedZero":false,"showThousandsSeparator":true,"shownIn":"ONES","suffix":"","symbolAlign":"SYMBOL DEFAULT","useParensForNegatives":false,"valueFormatType":"CURRENCY"}},"formats":{"cellFormat":{"backgroundColor":"#d0e8ff","borders":{"bottom":{"color":"#000","style":"SINGLE","weight":1},"left":{"color":"#000","style":"SINGLE","weight":1},"right":null,"top":{"color":"#000","style":"SINGLE","weight":1}},"horizontalAlign":null,"indent":null,"leaderDots":null,"textRotation":null,"verticalAlign":null},"textFormat":{"bold":true,"fontColor":null,"fontFamily":null,"fontSize":null,"italic":null,"strikethrough":null,"underline":null},"valueFormat":{"currencySymbol":{"currency":{"code":"EUR","display":"SYMBOL"},"generic":null},"dateAbbreviateMonth":null,"dateFormatString":null,"dateUppercaseAll":null,"displayZeroAs":"ZERO","enteredIn":"ONES","numbersAsWordsOptions":{"capitalizeFirstWord":false,"displayZeroAs":null},"percentSymbol":null,"periodFormat":null,"precision":{"auto":false,"value":2},"prefix":"","showCurrencySymbol":true,"showLeadingZero":true,"showNumbersAsWords":false,"showPositiveSign":null,"showSignRoundedZero":false,"showThousandsSeparator":true,"shownIn":"ONES","suffix":"","symbolAlign":null,"useParensForNegatives":false,"valueFormatType":"CURRENCY"}},"value":"=1+1"}]],"columnMetadata":[{"hidden":false,"size":75}],"merges":[{"startColumn":0,"startRow":0,"stopColumn":1,"stopRow":0}],"range":{"startColumn":0,"startRow":0,"stopColumn":0,"stopRow":0},"rowMetadata":[{"filtered":false,"hidden":false,"size":16}]},
        )
        """

    def testSheetDataResult(self):
        """Test SheetDataResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
