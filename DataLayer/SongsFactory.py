import json
import gzip
from elasticsearch import Elasticsearch


class SongFactory:
    ES_INDEX = "allsonglyrics"
    ES_TYPE = "song"

    def __init__(self):
        self.es = Elasticsearch()

    def get_songs_by_artist(self, artist_name):
        q = {
            "query": {
                "match": {
                    "_body.artist.unique_name": "Red_Hot_Chili_Peppers"
                }
            }
        }

        res = self.es.search(index=self.ES_INDEX, doc_type=self.ES_TYPE, body=q)
        parsed_result = [h["_source"]["_body"] for h in res["hits"]["hits"]]

        return parsed_result

"""
    def get_songs_by_artist(self, artist_name):
        DATA_URL = "/home/omri/Dev/Python/IntroToDS/Data/parsed_lyrics/{0}"
        songs_list = []

        with open(DATA_URL.format(artist_name), "rb") as data_file:
            songs_list = json.loads(gzip.decompress(data_file.read()).decode())

        return songs_list
"""