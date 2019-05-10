import random

from textrenderer.corpus.corpus import Corpus


class RandomCorpus(Corpus):
    """
    Load charsets and generate random word line from charsets
    """

    def load(self):
        pass

    def get_sample(self, img_index):
        word = ''
        indexes = []
        for _ in range(self.length):
            index = random.randint(0, len(self.charsets)) + 1
            indexes.append(index)
            word += self.charsets[index]
        return word, ' '.join([str(i) for i in indexes])

