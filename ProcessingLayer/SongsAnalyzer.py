import nltk
import DataLayer.SongsFactory as factory
import re


class SongsAnalyzer:
    WORDS_THRESHOLD = 30000

    def __init__(self):
        self.songs_factory = factory.SongFactory()

    def get_words_list_by_artist(self, artist_name):
        words = []
        for song in self.songs_factory.get_songs_by_artist(artist_name):
            #curr_lyrics = re.sub("[^A-Za-z0-9[.]]", "", song["lyrics"])
            #curr_lyrics = curr_lyrics.lower()
            curr_lyrics = nltk.word_tokenize(song["lyrics"])
            words += curr_lyrics

            if (len(words) >= self.WORDS_THRESHOLD):
                words = words[:self.WORDS_THRESHOLD]
                break

        return words
