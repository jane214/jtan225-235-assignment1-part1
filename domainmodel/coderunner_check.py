class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if not (isinstance(other, Director) or other.director_full_name is None):
            return False
        else:
            return self.director_full_name == other.director_full_name

    def __lt__(self, other):
        return self.director_full_name < other.director_full_name

    def __hash__(self):
        return hash(self.director_full_name)


class Actor:
    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.colleague = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    @actor_full_name.setter
    def actor_full_name(self, value):
        if value == "" or type(value) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = value.strip()

    def __repr__(self):
        return f"<Actor {self.actor_full_name}>"

    def __eq__(self, other):
        if not (isinstance(other, Actor) or other.actor_full_name is None):
            return False
        else:
            return self.actor_full_name == other.actor_full_name

    def __lt__(self, other):
        return self.actor_full_name < other.actor_full_name

    def __hash__(self):
        return hash(self.actor_full_name)

    def add_actor_colleague(self, colleague: "Actor"):
        self.colleague.append(colleague)

    def check_if_this_actor_worked_with(self, colleague: "Actor"):
        return colleague in self.colleague


class Genre:
    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    @genre_name.setter
    def genre_name(self, value):
        if value == "" or type(value) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = value.strip()

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if not (isinstance(other, Genre) or other.genre_name is None):
            return False
        else:
            return self.genre_name == other.genre_name

    def __lt__(self, other):
        return self.genre_name < other.genre_name

    def __hash__(self):
        return hash(self.genre_name)


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


# movie = Movie("Moana", 1900)
# print(movie)
#
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
# genre1 = Genre("tedtyd")
# movie.add_genre(genre1)
# print("genres", movie.genres)
# movie.remove_genre(genre1)
# print("genres sfter", movie.genres)
# movie2 = Movie("Mna", 2016)
# print(movie == movie2)
# print(movie.actors)
# print(movie.genres)
#
# movie.runtime_minutes = 100
# print("Movie runtime: {} minutes".format(movie.runtime_minutes))
# print(movie > movie2)
# d = dict()
# d[movie] = 2
# print(d)
