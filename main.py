from Tasks.AnalysisTasks import AnalysisTasks

def main():
    print("Songs Analyzer Project")
    tasks = AnalysisTasks()

    #tasks.compare_oriental_to_israeli()
    tasks.analyze_hip_hop()
    tasks.analyze_pop()
    #tasks.analyze_years([(1970, 1979), (1980, 1989), (1990, 1999), (2000, 2009)])

if __name__ == '__main__':
    main()
