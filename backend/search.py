from typing import List

from simstring.feature_extractor.character_ngram import CharacterNgramFeatureExtractor
from simstring.measure.cosine import CosineMeasure
from simstring.database.dict import DictDatabase
from simstring.searcher import Searcher

from util import DictItem, ManbyoSearcher, load_dic

class DiseaseSeacher(ManbyoSearcher):
    def __init__(self, dic: List[DictItem]):
        self.dic = dic
        self.db = DictDatabase(CharacterNgramFeatureExtractor(2))
        self._create_db(dic)
        self.searcher = Searcher(self.db, CosineMeasure())

    def _create_db(self, dic):
        self.name2item = {}
        for item in dic:
            self.db.add(item.name)
            self.name2item[item.name] = item

    def search(self, word):
        disease = set()
        output = []
        results = self.searcher.ranked_search(word, 0.4)
        for score, r in results:
            result = self.name2item[r]
            if result.norm == "-1":
                continue

            if result.norm not in disease:
                output.append(result)
                disease.add(result.norm)

        return output




if __name__ == "__main__":
    dic = load_dic("resource/dic.csv")
    searcher = DiseaseSeacher(dic)
    print(searcher.search("急性骨髄性"))

