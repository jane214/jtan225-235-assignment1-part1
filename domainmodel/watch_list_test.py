from datetime import date
import pytest

from domainmodel.movie import Movie
from domainmodel.watchlist import WatchList


@pytest.fixture()
def watchlist():
    watchlist = WatchList()
    watchlist.add_movie(Movie("Moana", 2016))
    watchlist.add_movie(Movie("Ice Age", 2002))
    return watchlist


def test_watchlist_construction():
    watchlist = WatchList()
    assert watchlist.size() == 0
    assert watchlist.watch_list == []


def test_add_movie(watchlist):
    assert watchlist.watch_list == [Movie("Moana", 2016), Movie("Ice Age", 2002)]


def test_add_error_movie(watchlist):
    watchlist.add_movie(" ")
    assert watchlist.watch_list == [Movie("Moana", 2016), Movie("Ice Age", 2002)]


def test_select_movie_to_watch(watchlist):
    movie3 = watchlist.select_movie_to_watch(0)
    assert watchlist.size() == 2
    assert movie3 == Movie("Moana", 2016)


def test_select_movie_to_watch_out_of_bound(watchlist):
    movie3 = watchlist.select_movie_to_watch(2)
    assert movie3 is None


def test_remove_movie_inside_list(watchlist):
    watchlist.remove_movie(Movie("Ice Age", 2002))
    assert watchlist.watch_list == [Movie("Moana", 2016)]


def test_remove_movie_not_inside_list(watchlist):
    watchlist.remove_movie(Movie("Guardians of the Galaxy", 2012))
    assert watchlist.watch_list == [Movie("Moana", 2016), Movie("Ice Age", 2002)]


def test_size(watchlist):
    assert watchlist.size() == 2


def test_first_movie_in_watchlist_not_empty(watchlist):
    assert watchlist.select_movie_to_watch(0) == Movie("Moana", 2016)


def test_first_movie_in_watchlist_is_empty():
    watchlist = WatchList()
    assert watchlist.select_movie_to_watch(0) is None


def test_iter(watchlist):
    num = 0
    if Movie("Moana", 2016) in watchlist.watch_list:
        num = 1
    assert num == 1


def test_iter_2(watchlist):
    num = 0
    for i in watchlist:
        num += 1
    assert num == watchlist.size()
