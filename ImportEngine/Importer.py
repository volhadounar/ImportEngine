from typing import List

from .ImportInterface import ImporterInterface
from .Cat import Cat
from .DocxImporter import DocxImporter
from .CSVImporter import CSVImporter


class Importer(ImporterInterface):
    importers = [DocxImporter, CSVImporter]

    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)