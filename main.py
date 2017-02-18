import ProcessingLayer.SongsAnalyzer as analyzer

def main():
    print("Songs Analyzer")
    rappers_list = ["kool_keith", "canibus", "cunninlynguists", "rza", "wu-tang", "killah_priest", "Drake"]

    songs_analyzer = analyzer.SongsAnalyzer()

    for artist in rappers_list:
        diversity = songs_analyzer.lexical_diversity_by_artist(artist)
        print("Rapper: {0} has lexical diversity of {1}".
              format(artist, diversity))


if __name__ == '__main__':
    main()
