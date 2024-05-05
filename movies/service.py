from movies.repository import MovieRepository


class MovieService:

    def __init__(self):
        self.movie_repository = MovieRepository()

    def get_movies(self):
        return self.movie_repository.get_movies()

    def create_movie(self, title, genre, release_date, actors, resume):
        new_movie = dict(
            title=title,
            genre=genre,
            release_date=release_date,
            actors=actors,
            resume=resume
        )

        return self.movie_repository.create_movie(new_movie)
