from typing import List

from domainmodel.movie import Movie


class WatchList:
    def __init__(self):
        self.__watchlist: List[Movie] = []

    @property
    def watch_list(self):
        return self.__watchlist

    @watch_list.setter
    def watch_list(self, new_list: list):
        self.__watchlist = new_list

    def add_movie(self, movie: Movie):
        if isinstance(movie, Movie):
            self.__watchlist.append(movie)

    def remove_movie(self, movie: Movie):
        if isinstance(movie, Movie) and movie in self.__watchlist:
            self.__watchlist.remove(movie)

    def select_movie_to_watch(self, index):
        if type(index) is not int or index >= len(self.__watchlist):
            return None
        else:
            return self.__watchlist[index]

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        if len(self.__watchlist) == 0:
            return None
        else:
            return self.__watchlist[0]

    def __repr__(self):
        return ", ".join(str(x) for x in self.__watchlist)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.__watchlist):
            result = self.__watchlist[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

# watchlist = WatchList()
# print(f"Size of watchlist: {watchlist.size()}")
# watchlist.add_movie(Movie("Moana", 2016))
# watchlist.add_movie(Movie("Ice Age", 2002))
# watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
# print(watchlist.size())
#
# for i in watchlist:
#     print(i)
