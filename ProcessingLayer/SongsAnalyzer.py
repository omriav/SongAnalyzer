import nltk
from nltk.stem import PorterStemmer
import DataLayer.SongsFactory as factory
import re


class SongsAnalyzer:
    WORDS_THRESHOLD = 4000

    def __init__(self):
        self.songs_factory = factory.SongFactory()

    def get_words_list_by_artist(self, artist_name):
        words = []
        words2 = []
        for song in self.songs_factory.get_songs_by_artist(artist_name):
            curr_lyrics = re.sub("[^\w]", " ", song["lyrics"])
            words += curr_lyrics.split()

            if (len(words) >= self.WORDS_THRESHOLD):
                words = words[:self.WORDS_THRESHOLD]
                break

        if (len(words) < self.WORDS_THRESHOLD):
            raise Exception("Artist '{0}' has only {1} words. Instead of {1} words".
                            format(artist_name, len(words), self.WORDS_THRESHOLD))

        return words

    def lexical_diversity_by_artist(self, artist_name):
        tokens = self.get_words_list_by_artist(artist_name)
        stemmer = PorterStemmer()
        stemmedTokens = [stemmer.stem(token) for token in tokens]
        types = set(stemmedTokens)

        type_token_ratio = len(types) / len(stemmedTokens)

        return type_token_ratio

