from typing import List

from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director



class Movie:
    def __init__(self, movie_name, release_year=None):
        if movie_name == "" or type(movie_name) is not str:
            self.__movie_name = None
        else:
            self.__movie_name = movie_name.strip()
        if type(release_year) is not int or release_year < 1900:
            self.__year = None
        else:
            self.__year = release_year
        self._description = None
        self._director = None
        self._actors = []
        self._genres = []
        self._runtime_minutes = None

    @property
    def year(self):
        return self.__year

    @property
    def title(self):
        return self.__movie_name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_string: str):
        if new_string == "" or type(new_string) is not str:
            self._description = None
        else:
            self._description = new_string.strip()

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, new_direct: Director):
        if isinstance(new_direct, Director):
            self._director = new_direct

    @property
    def actors(self):
        return self._actors

    @actors.setter
    def actors(self, new_actor: Actor):
        if isinstance(new_actor, Actor):
            self._actors = new_actor

    @property
    def genres(self):
        return self._genres

    @genres.setter
    def genres(self, new_genre: Genre):
        if isinstance(new_genre, Genre):
            self._genres = new_genre

    @property
    def runtime_minutes(self):
        return self._runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, new_runtime: int):
        if isinstance(new_runtime, int):
            if new_runtime > 0:
                self._runtime_minutes = new_runtime
            else:
                raise ValueError
        else:
            raise ValueError

    def concate(self) -> str:
        return str(self.__movie_name) + str(self.__year)

    def __repr__(self):
        return f"<Movie {self.__movie_name}, {self.__year}>"

    def __eq__(self, other: "Movie"):
        if not isinstance(other, Movie):
            return False
        else:
            string1 = self.concate()
            string2 = other.concate()
            return string1 == string2

    def __lt__(self, other):
        if isinstance(other, Movie):
            string1 = self.concate()
            string2 = other.concate()
            return string1 < string2

    def __str__(self):
        return f"<Movie {self.__movie_name}, {self.__year}>"

    def __hash__(self):
        string1 = self.concate()
        return hash(string1)

    def add_actor(self, new_actor: Actor):
        if isinstance(new_actor, Actor):
            self._actors.append(new_actor)

    def remove_actor(self, new_actor: Actor):
        if isinstance(new_actor, Actor) and new_actor in self._actors and (len(self._actors) > 0):
            self._actors.remove(new_actor)

    def add_genre(self, new_genre: Genre):
        if isinstance(new_genre, Genre):
            self._genres.append(new_genre)

    def remove_genre(self, new_genre: Genre):
        if isinstance(new_genre, Genre) and new_genre in self._genres and (len(self._genres) > 0):
            self._genres.remove(new_genre)


movie = Movie("Moana", 1900)

# print(movie)
# movie.actors = [1,2,3]
# director = Director("Ron Clements")
# movie.director = director
# print(movie.director)
# movie.director = Director("a")
# print(movie.director)
# actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
# for actor in actors:
#     movie.add_actor(actor)
# print(movie.actors)
# actor1 = Actor("")
# movie.remove_actor(Actor("Auli'i Cravalho"))
# genre1 = Genre("")
# movie.remove_genre(genre1)
# movie2 = Movie("Mna", 2016)
# print(movie == movie2)
# print(movie.actors)
# print(movie.genres)
# movie.description =""
# print(movie.description)
#
# # movie.runtime_minutes = 0
# print("Movie runtime: {} minutes".format(movie.runtime_minutes))
# print(movie > movie2)
# d = dict()
# d[movie] = 2
# print(d)
# movie8 = Movie("None", None)
# print(movie8.concate())
