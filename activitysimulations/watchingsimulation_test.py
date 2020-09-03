import pytest

from activitysimulations.watchingsimulation import MovieWatchingSimulation
from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.user import User
from domainmodel.watchlist import WatchList


@pytest.fixture()
def watchlist():
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    return watchlist


@pytest.fixture()
def movie():
    return Movie("Moana", 2016)


@pytest.fixture()
def user1():
    return User('Martin', 'pw12345')


@pytest.fixture()
def user2():
    return User('Ian', 'pw67890')


def test_add_user(movie, user1, user2):
    set1 = set()
    watch_together = MovieWatchingSimulation(movie)
    watch_together.add_user(user1)
    watch_together.add_user(user2)
    set1.add(user1)
    set1.add(user2)
    assert watch_together.user_set == set1

def test_write_review(movie,user1, user2):
    review_text = "This movie was very enjoyable."
    rating = 8
    review = Review(movie, review_text, rating)
    review_text3 = "This movie was very enjoyable."
    rating3 = 8
    review3 = Review(movie, review_text3, rating3)
    watch_together = MovieWatchingSimulation(movie)
    watch_together.add_user(user1)
    watch_together.add_user(user2)
    watch_together.write_review(user1, review_text, rating)
    watch_together.write_review(user2, review_text3, rating3)
    assert (watch_together.review_dict[user1] == review) == True
    assert (watch_together.review_dict[user2] == review3) == True


