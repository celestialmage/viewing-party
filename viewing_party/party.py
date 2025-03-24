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


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

