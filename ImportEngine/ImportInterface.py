from abc import ABC, abstractmethod
from .Cat import Cat

from typing import List
class ImporterInterface(ABC):
    
    allowed_extentions = []
    
    @classmethod
    def can_ingest(cls, path):
        ext = path.split('.')[-1]
        print(ext, cls.allowed_extentions)
        return ext in cls.allowed_extentions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[Cat]:
        ...
    