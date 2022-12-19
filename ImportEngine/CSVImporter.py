from typing import List
import pandas

from .ImportInterface import ImporterInterface
from .Cat import Cat

class CSVImporter(ImporterInterface):
    allowed_extentions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        cats = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_cat = Cat(row['Name'], row['Age'], row['isIndoor'])
            cats.append(new_cat)

        return cats