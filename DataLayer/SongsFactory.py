from elasticsearch import Elasticsearch


class SongFactory:
    ES_INDEX = "allsonglyrics"
    ES_TYPE = "song"

    def __init__(self):
        self.es = Elasticsearch()

    def parse_results(self, results):
        parsed_result = [h["_source"]["_body"] for h in results["hits"]["hits"]]

        return parsed_result

    def execute_es_query(self, query):
        res = self.es.search(index=self.ES_INDEX, doc_type=self.ES_TYPE, body=query)

        return self.parse_results(res)

    def get_songs_by_artist(self, artist_name):
        q = {
            "query": {
                "match": {
                    "_body.artist.unique_name": "{0}".format(artist_name)
                }
            },
            "size": 500
        }

        return self.execute_es_query(q)

    def get_songs_by_year_interval(self, start_year, end_year):
        q = {
            "query": {
                "range": {
                    "_body.album.year": {
                        "gte": start_year,
                        "lte": end_year
                    }
                }
            },
            "size": 5000
        }

        return self.execute_es_query(q)
