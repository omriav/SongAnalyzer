import ProcessingLayer.SongsAnalyzer as analyzer
from Model.MusicGenre import MusicGenre
import Configuration.ConfigurationManager as cfg


class AnalysisTasks:
    def calculate_average_diversity_by_gnere(self, full_artists_list, music_gnere):
        filtered_artists = [artist for artist in full_artists_list if artist.music_genre == music_gnere]
        diversity_sum = sum(artist.diversity_score for artist in filtered_artists)
        diversity_average = diversity_sum / len(filtered_artists)

        return diversity_average

    def compare_oriental_to_israeli(self):
        songs_analyzer = analyzer.SongsAnalyzer(cfg.HEBREW_ARTIST_WORD_THRESHOLD,
                                                cfg.HEBREW_YEAR_WORD_THRESHOLD)

        hebrew_artists_list = cfg.HEBREW_ARTIST_LIST

        for artist in hebrew_artists_list:
            artist.diversity_score = songs_analyzer.lexical_diversity_by_artist(artist.name)

        hebrew_artists_list.sort(key=lambda x: x.diversity_score)
        for artist in hebrew_artists_list:
            print("{0}({1}) has lexical diversity of {2}".
                  format(artist.name, artist.music_genre.name, artist.diversity_score))

        israeli_average = self.calculate_average_diversity_by_gnere(hebrew_artists_list, MusicGenre.Israeli)
        oriental_average = self.calculate_average_diversity_by_gnere(hebrew_artists_list, MusicGenre.Oriental)
        print("\nIsraeli average diversity score: " + str(israeli_average))
        print("Oriental average diversity score: " + str(oriental_average))

    def analyze_hip_hop(self):
        songs_analyzer = analyzer.SongsAnalyzer(cfg.ENGLISH_ARTIST_WORD_THRESHOLD,
                                                cfg.HEBREW_YEAR_WORD_THRESHOLD)

        hiphop_artist_list = cfg.HIPHOP_ARTIST_LIST
        for artist in hiphop_artist_list:
            artist.diversity_score = songs_analyzer.lexical_diversity_by_artist(artist.name)

        hiphop_artist_list.sort(key=lambda x: x.diversity_score)
        for artist in hiphop_artist_list:
            print("{0}({1}) has lexical diversity of {2}".
                  format(artist.name, artist.music_genre.name, artist.diversity_score))
