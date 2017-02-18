import ProcessingLayer.SongsAnalyzer as analyzer

def main():
    print("Songs Analyzer")
    songs_analyzer = analyzer.SongsAnalyzer()
    songs_analyzer.get_words_list_by_artist("Red_Hot_Chili_Peppers")


if __name__ == '__main__':
    main()
