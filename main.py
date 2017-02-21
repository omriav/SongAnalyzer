import ProcessingLayer.SongsAnalyzer as analyzer


def main():
    print("Songs Analyzer Project")
    songs_analyzer = analyzer.SongsAnalyzer()

    final_hebrew_list = []
    hebrew_list = ["Idan Raichel", "Eviatar Banai", "Moshe Peretz", "Dudu Aharon", "Kobi Peretz",
                   "Meir Ariel", "Hadag Nahash", "Lior Narkis", "Mooki", "Eyal Golan", "Omer Adam",
                   "Regev Hod", "Sarit Hadad", "Shlomo Artzi", "Shalom Hanoch", "Arik Einstein",
                   "Rita", "Miri Mesika", "Keren Peles", "Assaf Amdursky", "Avraham Tal",
                   "Mashina", "Yehoram Gaon"]
    hebrew_diversity_sum = 0
    for artist in hebrew_list:
        diversity = songs_analyzer.lexical_diversity_by_artist(artist)
        hebrew_diversity_sum += diversity
        final_hebrew_list.append({
            "name": artist,
            "score": diversity
        })

    final_hebrew_list.sort(key=lambda x: x['score'])
    for artist_total in final_hebrew_list:
        print("Hebrew artist: {0} has lexical diversity of {1}".
              format(artist_total["name"], artist_total["score"]))

    hebrew_diversity_avg = hebrew_diversity_sum / len(hebrew_list)
    print("\nAverage diversity for hebrew artists: {0}\n".format(hebrew_diversity_avg))

    """
    rappers_list = ["kool_keith", "canibus", "cunninlynguists", "rza", "wu-tang", "killah_priest", "eminem"]
    rappers_diversity_sum = 0
    for artist in rappers_list:
        diversity = songs_analyzer.lexical_diversity_by_artist(artist)
        rappers_diversity_sum += diversity
        print("Rapper: {0} has lexical diversity of {1}".
              format(artist, diversity))
    rappers_diversity_avg = rappers_diversity_sum / len(rappers_list)
    print("Average diversity for rappers: {0}\n".format(rappers_diversity_avg))


    pop_artists = ["lady_gaga", "big_sean", "ed_sheeran", "bruno_mars", "drake",
                   "migos", "rihanna", "adele", "twenty_one_pilots",
                   "ariana_grande", "taylor_swift", "maroon_5", "justin_bieber",
                   "imagine_dragons", "john_legend", "metallica", "sia", "train"]
    pop_diversity_sum = 0
    for artist in pop_artists:
        diversity = songs_analyzer.lexical_diversity_by_artist(artist)
        pop_diversity_sum += diversity
        print("Artist: {0} has lexical diversity of {1}".
              format(artist, diversity))
    pop_diversity_avg = pop_diversity_sum / len(pop_artists)
    print("Average diversity for pop artists is: {0}".format(pop_diversity_avg))


    years_intervals = [(1970, 1979), (1980, 1989), (1990, 1999), (2000, 2009)]
    for year_interval in years_intervals:
        diversity = songs_analyzer.lexical_diversity_by_year_interval(year_interval[0], year_interval[1])
        print("Interval {0}-{1} has diversity of: {2}".format(year_interval[0], year_interval[1], diversity))
    """

if __name__ == '__main__':
    main()
