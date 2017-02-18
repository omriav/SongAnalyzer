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
                    "_body.artist.unique_name": "{0}".format(artist_name)
                }
            }
        }

        res = self.es.search(index=self.ES_INDEX, doc_type=self.ES_TYPE, body=q)
        parsed_result = [h["_source"]["_body"] for h in res["hits"]["hits"]]

        return parsed_result