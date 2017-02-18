import ProcessingLayer.SongsAnalyzer as analyzer

def main():
    print("Songs Analyzer")
    songs_analyzer = analyzer.SongsAnalyzer()
    songs_analyzer.lexical_diversity_by_artist("Kool_keith")


if __name__ == '__main__':
    main()
