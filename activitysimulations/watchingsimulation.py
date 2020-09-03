from typing import Set

from domainmodel.movie import Movie
from domainmodel.user import User
from domainmodel.review import Review
from domainmodel.watchlist import WatchList


class MovieWatchingSimulation:
    def __init__(self, movie: Movie):
        self.__user_set: Set[User] = set()
        self.__movie_to_watch: Movie = movie
        self.__review_dict = {}

    @property
    def user_set(self):
        return self.__user_set

    @property
    def movie_to_watch(self):
        return self.__movie_to_watch

    @property
    def review_dict(self):
        return self.__review_dict

    @property
    def size(self):
        return len(self.__user_set)

    def add_user(self, user: User):
        if isinstance(user, User):
            self.__user_set.add(user)
            if self.__movie_to_watch in user.watch_list:
                user.watch_list.remove_movie(self.__movie_to_watch)

    def get_together(self, user_list):
        for i in user_list:
            self.add_user(i)

    def write_review(self, user: User, text, rating_num):
        review = Review(self.__movie_to_watch, text, rating_num)
        if isinstance(user, User) and user in self.__user_set:
            user.add_review(review)
            self.__review_dict[user] = review


user1 = User('Martin', 'pw12345')
user2 = User('Ian', 'pw67890')
movie = Movie("Moana", 2016)
watchlist = WatchList()
watchlist.add_movie(Movie("Moana", 2016))
watchlist.add_movie(Movie("Ice Age", 2002))
user1.watch_list = watchlist
print("init user watch list", watchlist)
watch_together = MovieWatchingSimulation(movie)
print("movie to watch", watch_together.movie_to_watch)
watch_together.add_user(user1)
watch_together.add_user(user2)
print(watch_together.size)
print("after", user1.watch_list)
review_text = "This movie was very enjoyable."
rating = 8
review = Review(movie, review_text, rating)
review_text3 = "This movie was very enjoyable."
rating3 = 8
review3 = Review(movie, review_text3, rating3)
watch_together = MovieWatchingSimulation(movie)
list1 = []
list1.append(user1)
list1.append(user2)
watch_together.get_together((list1))
watch_together.write_review(user1, review_text, rating)
watch_together.write_review(user2, review_text3, rating3)
print(watch_together.review_dict[user1])

