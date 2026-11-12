"""Movie information shared by multiple showtimes."""


class Movie:
    def __init__(self, movie_id: str, title: str) -> None:
        self.movie_id = movie_id
        self.title = title
