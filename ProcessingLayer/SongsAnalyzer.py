from nltk.stem import PorterStemmer
import DataLayer.SongsFactory as factory
import re


class SongsAnalyzer:
    def __init__(self, artist_words_threshold, year_words_threshold):
        self.songs_factory = factory.SongFactory()
        self.ARTIST_WORDS_THRESHOLD = artist_words_threshold
        self.YEAR_WORDS_THRESHOLD = year_words_threshold

    def calculate_lexical_diversity(self, tokens):
        stemmer = PorterStemmer()
        stemmed_tokens = [stemmer.stem(token) for token in tokens]
        types = set(stemmed_tokens)

        type_token_ratio = len(types) / len(stemmed_tokens)

        return type_token_ratio

    def convert_songs_to_words_bag(self, songs, threshold=-1):
        words = []

        for song in songs:
            curr_lyrics = re.sub("[^\w]", " ", song["lyrics"])
            words += curr_lyrics.split()

            if threshold != -1:
                if len(words) >= threshold:
                    words = words[:threshold]
                    break

        return words

    def threshold_checker(self, words, threshold, message):
        if len(words) < threshold:
            raise Exception(message)

    def get_words_list_by_artist(self, artist_name):
        songs_by_artist = self.songs_factory.get_songs_by_artist(artist_name)
        words = self.convert_songs_to_words_bag(songs_by_artist, self.ARTIST_WORDS_THRESHOLD)

        self.threshold_checker(words, self.ARTIST_WORDS_THRESHOLD,
                               "Artist '{0}' has only {1} words. Instead of {2} words".
                               format(artist_name, len(words), self.ARTIST_WORDS_THRESHOLD))

        return words

    def lexical_diversity_by_artist(self, artist_name):
        tokens = self.get_words_list_by_artist(artist_name)

        return self.calculate_lexical_diversity(tokens)

    def get_words_list_by_year(self, start_year, end_year):
        songs_by_years_interval = self.songs_factory.get_songs_by_year_interval(start_year, end_year)
        words = self.convert_songs_to_words_bag(songs_by_years_interval, self.YEAR_WORDS_THRESHOLD)

        self.threshold_checker(words, self.YEAR_WORDS_THRESHOLD,
                               "Years interval {0}-{1} has {2} words (minimum words is {3})".
                               format(start_year, end_year, len(words), self.YEAR_WORDS_THRESHOLD))

        return words

    def lexical_diversity_by_year_interval(self, start_year, end_year):
        tokens = self.get_words_list_by_year(start_year, end_year)

        return self.calculate_lexical_diversity(tokens)
