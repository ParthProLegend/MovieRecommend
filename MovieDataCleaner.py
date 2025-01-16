def DataCleanerService():
    # j = 0

    # OriginalFile = "Inside Lab\\WWC_24\\FinalProject\\OriginalMovieData\\title.basics.tsv"
    # File100 = "Inside Lab\\WWC_24\\FinalProject\\SampleData\\Titles100.tsv"
    # CompiledCategoryFile = "Inside Lab\\WWC_24\\FinalProject\\CompiledData\\CategoryData.txt"
    # MovieData = "Inside Lab\\WWC_24\\FinalProject\\CompiledData\\MovieData.txt"


    CompiledCategoryFile = "CategoryData.txt"
    MovieData = "MovieData.txt"


    # Clearing Old File Data or Creating New Files
    with open(CompiledCategoryFile, mode="w", encoding="utf-8") as dump:
        dump.write("")
        pass
    with open(MovieData, mode="w", encoding="utf-8") as dump:
        dump.write("")
        pass
    # with open(File100, mode="w", encoding="utf-8") as dump:
        # dump.write("")

    # Creating New Files With New Data
    # with open(OriginalFile, mode="r", encoding="utf-8") as data, open(File100, mode="a", encoding="utf-8") as newfiledata2:
    #     for EachLine in data:
    #         newfiledata2.write(EachLine)
    #         j += 1
    #         if j > 99:
    #             break