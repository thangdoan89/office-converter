import zipfile
from bs4 import BeautifulSoup
from office_converter.common.core.base_converter import Converter

class DocumentConverter(Converter):

    def toHtml(self) -> str:

        with zipfile.ZipFile(self.file_path) as unzipped_docx:
            result = unzipped_docx.namelist()
            print(result)
            document_data = unzipped_docx.read('word/document.xml')
            document_data = BeautifulSoup(document_data, "xml")
            output_children = ''
            for child in document_data.body.children:
                output_children += f'{child} \n'

    def toText(self) -> str:
        return super().toText()

    def toJson(self) -> str:
        return super().toJson()

