OriginalFile = "OriginalMovieData\\title.basics.tsv"
MovieData = "MovieData.txt"


def FindMostLikedMovieCategories(movie_liked_list=dict, categories_liked=dict):
    movie_categories = dict()

    with open(MovieData, mode="r", encoding="utf-8") as CompiledMovieData:
        temp = CompiledMovieData.read().strip()
        if temp == "":
            MovieDictionaryCreator()
    with open(MovieData, mode="r", encoding="utf-8") as CompiledMovieData:
        for EachLine in CompiledMovieData:
            (key, value) = EachLine.split("\t", 1)
            movie_categories[key] = value

    for EachMovie in movie_liked_list:
        # Create a dictionary with movie id as keys and categories as values
        categories = movie_categories[EachMovie[0]].split(",")
        for EachCategory in categories:
            EachCategory = EachCategory.strip()
            if EachCategory == r"\N":
                EachCategory = "Undefined"
            if EachCategory == "":
                continue
            categories_liked[EachCategory] += float(EachMovie[1])
    return categories_liked


def MovieDictionaryCreator():
    TempDictionary = {}
    r = open(MovieData, mode="w", encoding="utf-8")
    o = 0
    with open(OriginalFile, mode="r", encoding="utf-8") as data:
        for EachLine in data:
            if o == 0:
                o += 1
                continue
            # (key, value) = EachLine.split("\t", 1)
            # value = value.split("\t")
            # value = value[:3] + value[4:]
            # value = value[:4] + value[6:]
            # TempDictionary[key] = value

            (key, value) = EachLine.split("\t", 1)
            value = (value.split("\t"))[-1].strip()
            TempDictionary[key] = value
            r.write(f"{key}\t{value}\n")

    r.close()


def MovieNameTeller(movies_list=list):
    TempDictionary = dict()
    movies = list()
    with open(OriginalFile, mode="r", encoding="utf-8") as data:
        for EachLine in data:
            (key, value) = EachLine.split("\t", 1)
            value = value.split("\t", 2)
            value = value[1]
            TempDictionary[key] = value

    for movie_id in movies_list:
        movies.append(TempDictionary[movie_id])

    return movies
