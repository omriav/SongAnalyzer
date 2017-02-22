import ProcessingLayer.SongsAnalyzer as analyzer
from Model.Artist import Artist
from Model.MusicGenre import MusicGenre

class AnalysisTasks:
    def calculate_average_diversity_by_gnere(self, full_artists_list, music_gnere):
        filtered_artists = [artist for artist in full_artists_list if artist.music_genre == music_gnere]
        diversity_sum = sum(artist.diversity_score for artist in filtered_artists)
        diversity_average = diversity_sum / len(filtered_artists)

        return diversity_average

    def compareOrieantalToIsraeli(self):
        songs_analyzer = analyzer.SongsAnalyzer()

        hebrew_artists_list = [
            Artist("Idan Raichel", MusicGenre.Israeli),
            Artist("Eviatar Banai", MusicGenre.Israeli),
            Artist("Moshe Peretz", MusicGenre.Oriental),
            Artist("Dudu Aharon", MusicGenre.Oriental),
            Artist("Kobi Peretz", MusicGenre.Oriental),
            Artist("Meir Ariel", MusicGenre.Israeli),
            Artist("Hadag Nahash", MusicGenre.Israeli),
            Artist("Lior Narkis", MusicGenre.Oriental),
            Artist("Mooki", MusicGenre.Israeli),
            Artist("Eyal Golan", MusicGenre.Oriental),
            Artist("Omer Adam", MusicGenre.Oriental),
            Artist("Regev Hod", MusicGenre.Oriental),
            Artist("Sarit Hadad", MusicGenre.Oriental),
            Artist("Shlomo Artzi", MusicGenre.Israeli),
            Artist("Shalom Hanoch", MusicGenre.Israeli),
            Artist("Arik Einstein", MusicGenre.Israeli),
            Artist("Rita", MusicGenre.Israeli),
            Artist("Miri Mesika", MusicGenre.Israeli),
            Artist("Keren Peles", MusicGenre.Israeli),
            Artist("Assaf Amdursky", MusicGenre.Israeli),
            Artist("Avraham Tal", MusicGenre.Israeli),
            Artist("Mashina", MusicGenre.Israeli),
            Artist("Yehoram Gaon", MusicGenre.Israeli),
        ]

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