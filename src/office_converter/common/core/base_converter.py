from abc import ABC, abstractmethod


class Converter(ABC):
    file_path: str

    @abstractmethod
    def toHtml(self) -> str: pass

    @abstractmethod
    def toText(self) -> str: pass

    @abstractmethod
    def toJson(self) -> str: pass