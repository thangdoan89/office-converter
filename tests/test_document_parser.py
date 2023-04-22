import unittest
import logging

from office_converter.converters.document.converter import DocumentConverter


logger = logging.getLogger(__file__)

class TestDocumentConverter(unittest.TestCase):
    def test_convert_docx_file(self):
        logger.info('test logger')
        pass
