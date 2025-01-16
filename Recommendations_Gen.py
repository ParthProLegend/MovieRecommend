import MovieDatabase as CatFind
import MovieCategoryCompiler as CatCompiler
import MovieDataCleaner as DataCleaner

MovieData = "MovieData"

def FindRecommendations(user_watchlist=dict, user_choice="0"):
    DataCleaner.DataCleanerService()
    categories_liked_by_user = list()
    user_watchlist_titles = list(user_watchlist.keys())
    if user_choice == "0":
        categories_liked_list = CatCompiler.MovieCategoryAggregator()
        n = len(user_watchlist)
        user_watchlist = sorted(user_watchlist.items(), key=lambda x: x[1], reverse=True)
        most_liked = user_watchlist.copy()
        most_liked = most_liked[: n // 5]

        categories_liked = CatFind.FindMostLikedMovieCategories(most_liked, categories_liked_list)

        categories_liked = sorted(categories_liked.items(), key=lambda x: x[1], reverse=True)
        for i in range(5):
            categories_liked_by_user.append(categories_liked[i][0]) if categories_liked[i][1] > 0 else None
    # print("Categories liked: ", categories_liked)
    # print("\nCategories liked by user: ", categories_liked_by_user)

    number_of_recommended_movies = int(input("How many recommendations do you want?"))
    # number_of_recommended_movies = 10
    recommended_movies = list()
    with open(MovieData, mode="r", encoding="utf-8") as CompiledMovieData:
        for EachLine in CompiledMovieData:
            (key, value) = EachLine.split("\t", 1)
            value = value.strip().split(",")
            recommended_movies.append(key) if any(category in value for category in categories_liked_by_user) and key not in user_watchlist_titles else None

            if len(recommended_movies) >= number_of_recommended_movies:
                recommended_movies_titles = CatFind.MovieNameTeller(recommended_movies)
                print("Recommended Shows: ", recommended_movies_titles)
                break


# This test dictionary contains the movie IDs (ttxxxxxxx) and their ratings (out of 10)
test_dict = {
    "tt0000001": 1.00,
    "tt0000003": 1.00,
    "tt0500003": 1.02,
    "tt0005002": 3.76,
    "tt0040008": 2.64,
    "tt0030009": 1.50,
    "tt0007006": 1.90,
    "tt0600007": 6.40,
    "tt0080031": 8.60,
    "tt0090029": 9.90,
    "tt0800028": 9.89,
    "tt0700026": 1.065,
    "tt0080024": 9.90,
    "tt0760022": 1.035,
    "tt0830023": 4.00,
    "tt0563021": 6.0,
    "tt0007012": 7.90,
    "tt0900013": 9.10,
    "tt0080014": 3.70,
    "tt0008815": 7.80,
    "tt0086016": 1.69,
    "tt0093017": 6.9,
    "tt0000618": 1,
    "tt0007019": 1.07,
    "tt0568020": 1.054,
    "tt0054311": 1.078,
    "tt0034654": 1.803,
}


FindRecommendations(test_dict)
