# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {"title": title, "genre": genre, "rating": rating}
    return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            break
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total = 0

    for movie in user_data["watched"]:
        total += movie["rating"]

    if len(user_data["watched"]) != 0:
        total /= len(user_data['watched'])

    return total

def get_most_watched_genre(user_data):

    genre = {}

    for movie in user_data['watched']:
        if movie['genre'] in genre:
            genre[movie['genre']] += 1
        else:
            genre[movie['genre']] = 1

    if not genre:
        return None
    
    highest_count = 0
    most_watched = ""

    for genre, count in genre.items():
        if count > highest_count:
            highest_count = count
            most_watched = genre

    return most_watched

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

    user_movies = {}
    movies = []
    friends_movies = user_data['friends']

    for movie in user_data['watched']:

        user_movies[movie['title']] = True

    for movie_list in friends_movies:

        movies += movie_list['watched']

    for movie in movies:

        if movie['title'] in user_movies:

            user_movies[movie['title']] = False

    unique_movies = []

    for movie in user_data['watched']:
        if movie['title'] in user_movies and user_movies[movie['title']] == True:
            unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):

    # 1. Initialize Variables
    friends_movies = user_data['friends']
    movies = []

    # 2. Add all movies friends have watched to movies
    for movie_list in friends_movies:

        movies += movie_list['watched']

    # 3. Iterate through movies and remove movies user has watched

    unique_movies = []

    for movie in movies:

        if movie not in user_data['watched'] and movie not in unique_movies:
            unique_movies.append(movie)

    return unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):

    friends_unique_movies = get_friends_unique_watched(user_data)

    user_services = user_data["subscriptions"]

    rec_movies = []

    for movie in friends_unique_movies:
        if movie["host"] in user_services:
            rec_movies.append(movie)
    return rec_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------