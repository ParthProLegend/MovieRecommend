def DataCleanerService():

    CompiledCategoryFile = "CategoryData.txt"
    MovieData = "MovieData.txt"


    # Clearing Old File Data or Creating New Files
    with open(CompiledCategoryFile, mode="w", encoding="utf-8") as dump:
        dump.write("")
        pass
    with open(MovieData, mode="w", encoding="utf-8") as dump:
        dump.write("")
        pass
