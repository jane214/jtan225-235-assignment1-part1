import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self._dataset_of_movies = []
        self._genre_list = []
        self._actor_list = []
        self._director_list = []
        self._dataset_of_actors = set()
        self._dataset_of_genres = set()
        self._dataset_of_directors = set()

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                movie = Movie(title, release_year)
                self._dataset_of_movies.append(movie)
                self._genre_list += row['Genre'].split(",")
                self._actor_list += row["Actors"].split(',')
                self._director_list += row["Director"].split(',')

    @property
    def dataset_of_movies(self):
        return self._dataset_of_movies

    @property
    def dataset_of_actors(self):
        for act in self._actor_list:
            self._dataset_of_actors.add(Actor(act))
        return self._dataset_of_actors

    @property
    def dataset_of_directors(self):
        for direct in self._director_list:
            self._dataset_of_directors.add(Director(direct))
        return self._dataset_of_directors

    @property
    def dataset_of_genres(self):
        for genre in self._genre_list:
            self._dataset_of_genres.add(Genre(genre))
        return self._dataset_of_genres

#
# filename = 'Data1000Movies.csv'
# movie_file_reader1 = MovieFileCSVReader(filename)
# movie_file_reader1.read_csv_file()
#
# print(movie_file_reader1.dataset_of_actors)
# print(f'number of unique movies: {len(movie_file_reader1.dataset_of_movies)}')
# print(f'number of unique actors: {len(movie_file_reader1.dataset_of_actors)}')
# print(f'number of unique directors: {len(movie_file_reader1.dataset_of_directors)}')
# print(f'number of unique genres: {len(movie_file_reader1.dataset_of_genres)}')
