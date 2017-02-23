from Model.Artist import Artist
from Model.MusicGenre import MusicGenre

# For hebrew songs analysis
HEBREW_ARTIST_WORD_THRESHOLD = 4500
HEBREW_YEAR_WORD_THRESHOLD = 500000

HEBREW_ARTIST_LIST = [
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

# For english analysis
ENGLISH_ARTIST_WORD_THRESHOLD = 12000
ENGLISH_YEAR_WORD_THRESHOLD = 500000

HIPHOP_ARTIST_LIST = [
    Artist("Kool_Keith", MusicGenre.HipHop),
    Artist("Canibus", MusicGenre.HipHop),
    Artist("RZA", MusicGenre.HipHop),
    Artist("Killah_Priest", MusicGenre.HipHop),
    Artist("Eminem", MusicGenre.HipHop)
]

POP_ARTIST_LIST = [
    Artist("Lady_Gaga", MusicGenre.Pop),
    Artist("Big_Sean", MusicGenre.Pop),
    Artist("Ed_Sheeran", MusicGenre.Pop),
    Artist("Drake", MusicGenre.Pop),
    Artist("Migos", MusicGenre.Pop),
    Artist("Rihanna", MusicGenre.Pop),
    Artist("Adele", MusicGenre.Pop),
    Artist("Twenty_One_Pilots", MusicGenre.Pop),
    Artist("Ariana_Grande", MusicGenre.Pop),
    Artist("Taylor_Swift", MusicGenre.Pop),
    Artist("Maroon_5", MusicGenre.Pop),
    Artist("Justin_Bieber", MusicGenre.Pop),
    Artist("Imagine_Dragons", MusicGenre.Pop),
    Artist("John_Legend", MusicGenre.Pop),
    Artist("Metallica", MusicGenre.Pop),
    Artist("Sia", MusicGenre.Pop),
    Artist("Train", MusicGenre.Pop),
]