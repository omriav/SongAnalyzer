import json
import gzip


class SongFactory:


    def get_songs_by_artist(self, artist_name):
        DATA_URL = "/home/omri/Dev/Python/IntroToDS/Data/parsed_lyrics/{0}"
        songs_list = []

        with open(DATA_URL.format(artist_name), "rb") as data_file:
            songs_list = json.loads(gzip.decompress(data_file.read()).decode())

        return songs_list
