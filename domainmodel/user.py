from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.watchlist import WatchList


class User:
    def __init__(self, name: str, password: str):
        if name == "" or type(name) is not str:
            self.__user_name = None
        else:
            self.__user_name = name.strip().lower()
        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password
        self._watched_movies = []
        self._reviews = []
        self._time_spent = 0
        self._watch_list = WatchList()

    @property
    def user_name(self):
        return self.__user_name

    @property
    def password(self):
        return self.__password

    @property
    def watched_movies(self):
        return self._watched_movies

    @property
    def reviews(self):
        return self._reviews

    @property
    def watch_list(self):
        return self._watch_list

    @watch_list.setter
    def watch_list(self, list1):
        self._watch_list = list1

    @property
    def time_spent_watching_movies_minutes(self):
        return self._time_spent

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, value):
        if (type(value) is not int) or value < 0:
            self._time_spent = None
        else:
            self._time_spent = value

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        else:
            return self.__user_name == other.__user_name

    def __lt__(self, other):
        if isinstance(other, User):
            return self.__user_name < other.__user_name

    def __hash__(self):
        return hash(self.__user_name)

    def watch_movie(self, movie1: Movie):
        if isinstance(movie1, Movie) and movie1 not in self._watched_movies:
            self._watched_movies.append(movie1)
            if type(movie1.runtime_minutes) is int:
                self._time_spent += movie1.runtime_minutes

    def add_review(self, review1):
        if isinstance(review1, Review) and review1 not in self._reviews:
            self._reviews.append(review1)

    def add_watch_list(self, new_movie: Movie):
        if isinstance(new_movie, Movie):
            self._watch_list.add_movie(new_movie)

# user1 = User('Martin', 'pw12345')
# user2 = User('Ian', 'pw67890')
# movie1 = Movie("min", 2019)
# movie2 = Movie("ghn", 2019)
# user1.add_watch_list(movie1)
# user1.add_watch_list(movie2)
# for i in user1.watch_list:
#     print(i)
# print(user1.watch_list)
# print("aa")
# user3 = User('Daniel', 'pw87465')
# print(user1)
# print(user2)
# print(user3)
# movie = Movie("Moana", 2016)
# movie.runtime_minutes=100
# print(" " == user2)
# review_text = "This movie was very enjoyable."
# rating = 8
# review = Review(movie, review_text, rating)
# user1.add_review(review)
# user1.watch_movie(movie)
# movie1 = Movie("Mna", 2017)
# movie1.runtime_minutes= 80
# user1.add_review(("sds"))
# user1.watch_movie(movie1)
# print(user1.watched_movies)
# print(user1.user_name)
# print(user1.time_spent_watching_movies_minutes)
# print(user1.reviews)
# c = {}
# c[user1] =1
# print(c)
# c[user2] = 9
# print(c)

