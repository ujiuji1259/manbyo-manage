from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
import csv

class ManbyoSearcher(metaclass=ABCMeta):
    @abstractmethod
    def search(self, text):
        pass

@dataclass
class DictItem:
    name: str
    icd: str
    norm: str

def load_dic(path):
    dic = []
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            dic.append(DictItem(*row))

    return dic
