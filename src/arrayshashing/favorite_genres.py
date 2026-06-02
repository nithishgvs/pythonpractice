from collections import defaultdict
from typing import Dict, List

"""

    Given: Asked in Amazon

    - userSongs: maps each user to the list of songs they listened to.

    - songGenres: maps each genre to the list of songs in that genre.

    Each song belongs to at most one genre.

    Return:

    - A map where each user is mapped to their favorite genre(s).

    - A favorite genre is the genre with the highest number of listened songs for that user.

    - If multiple genres have the same highest count, include all of them.

    - If a user has no songs that belong to any genre, return an empty list for that user.

    Example:

    userSongs = {

        "David": ["song1", "song2", "song3", "song4", "song8"],

        "Emma": ["song5", "song6", "song7"]

    }

    songGenres = {

        "Rock": ["song1", "song3"],

        "Dubstep": ["song7"],

        "Techno": ["song2", "song4"],

        "Pop": ["song5", "song6"],

        "Jazz": ["song8", "song9"]

    }

    Output:

    {

        "David": ["Rock", "Techno"],

        "Emma": ["Pop"]

    }

    """


def favorite_genres(user_songs: dict[str, List[str]], song_genres: Dict[str, List[str]]) -> dict[str, List[str]]:
    # Build a reverse map: song -> genre
    # In Java: HashMap<String, String> songGenreMap = new HashMap<>();
    song_genre = {}
    for genre, songs in song_genres.items():   # .items() is like entrySet() in Java
        for song in songs:
            song_genre[song] = genre

    result = {}

    for user, songs in user_songs.items():
        # defaultdict(int) is like a HashMap where missing keys default to 0
        # In Java: Map<String, Integer> with getOrDefault(key, 0)
        genre_count = defaultdict(int)

        for song in songs:
            if song in song_genre:             # 'in' is like containsKey() in Java
                genre_count[song_genre[song]] += 1

        # max() with default=0 avoids ValueError when genre_count is empty
        max_count = max(genre_count.values(), default=0)

        # List comprehension — like a filtered stream in Java:
        # genre_count.entrySet().stream().filter(e -> e.getValue() == maxCount).map(Map.Entry::getKey).toList()
        result[user] = [g for g, c in genre_count.items() if c == max_count] if max_count > 0 else []

    return result


def test_favorite_genres():
    user_songs = {
        "David": ["song1", "song2", "song3", "song4", "song8"],
        "Emma": ["song5", "song6", "song7"]
    }

    song_genres = {
        "Rock": ["song1", "song3"],
        "Dubstep": ["song7"],
        "Techno": ["song2", "song4"],
        "Pop": ["song5", "song6"],
        "Jazz": ["song8", "song9"]
    }

    expected = {
        "David": ["Rock", "Techno"],
        "Emma": ["Pop"]
    }

    result = favorite_genres(user_songs, song_genres)

    assert result == expected