OriginalFile = "OriginalMovieData\\title.basics.tsv"
CompiledCategoryFile = "CategoryData.txt"


def MovieCategoryAggregator():
    categories_liked = dict()
    with open(CompiledCategoryFile, mode="r", encoding="utf-8") as CompiledMovieCategoryData:
        temp = CompiledMovieCategoryData.read().strip()
        if temp == "":
            MovieCategoryAggregatorSubProcess()
    with open(CompiledCategoryFile, mode="r", encoding="utf-8") as CompiledMovieCategoryData:
        for EachLine in CompiledMovieCategoryData:
            categories_liked[EachLine.strip()] = 0

    return categories_liked


def MovieCategoryAggregatorSubProcess():
    categories = list()
    with open(OriginalFile, mode="r", encoding="utf-8") as raw_data:
        for EachLine in raw_data:
            EachCategory = EachLine.split("\t")[-1].strip()
            EachCategory = EachCategory.split(",")
            for category in EachCategory:
                if category not in categories:
                    if category == "genres":
                        continue
                    categories.append(category.strip())
    with open(CompiledCategoryFile, mode="a", encoding="utf-8") as CompiledMovieData:
        for category in categories:
            category = "Undefined".strip() if category == r"\N" else category.strip()
            CompiledMovieData.write(category + "\n")
