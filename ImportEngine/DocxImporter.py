from typing import List
from docx import Document
from .ImportInterface import ImporterInterface
from .Cat import Cat

class DocxImporter(ImporterInterface):
    allowed_extentions = ['docx']
    
    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest', path)
        
        cats = []
        doc = Document(path)
        for el in doc.paragraphs:
            if el.text != "":
                parse = el.text.split(',')
                new_cat = Cat(parse[0], int(parse[1]), bool(parse[2]))
                cats.append(new_cat)
        return cats
            