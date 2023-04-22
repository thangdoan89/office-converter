from abc import ABC, abstractmethod
from office_converter.common.statics.constants import ResponseMessage


class Converter(ABC):
    file_path: str
    output_encoding: str
    output_data: str
    output_path: str
    split_images: bool

    def __init__(self, filepath: str, output_path: str = None, split_images: bool = False, output_encoding: str = 'utf-8') -> None:
        self.file_path = filepath
        self.output_path = output_path
        self.split_images = split_images
        self.output_encoding = output_encoding

    def save(self):
        if not self.output_path:
            return self.output_data

        with open(self.output_path, 'w', encoding=self.output_encoding) as output_file:
            output_file.write(self.output_data)
            return ResponseMessage.CONVERSION_DONE.value


    @abstractmethod
    def toHtml(self) -> str: pass

    @abstractmethod
    def toText(self) -> str: pass

    @abstractmethod
    def toJson(self) -> str: pass