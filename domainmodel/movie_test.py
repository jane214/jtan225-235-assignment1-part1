import pytest

from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.genre import Genre
from domainmodel.movie import Movie


class Test_Movie_Methods:
    # @pytest.fixture
    def test_init(self):
        movie1 = Movie("Moana", 2016)
        assert repr(movie1) == "<Movie Moana, 2016>"
        movie2 = Movie("")
        assert movie2.title is None
        assert movie2.year is None
        movie3 = Movie(3)
        assert movie3.title is None
        movie1.director = "er"
        assert movie1.director is None
        movie4 = Movie("Moana", 2016)
        movie5 = Movie("Mn", 2017)
        assert (movie1 == movie5) == False
        assert (movie1 == movie4) == True
        assert movie1.title == "Moana"
        assert movie1.description == None
        movie1.description = 2
        assert movie1.description == None
        movie1.description = "adcsdv"
        assert movie1.description == "adcsdv"
        movie1.director = "as"
        assert movie1.director is None
        movie1.director = Director("asd")
        assert (movie1.director == Director("asd")) == True
        actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
        for actor in actors:
            movie1.add_actor(actor)
        movie6 = Movie("as", 190)
        genres = [Genre("asdc"), Genre("dfg")]
        for genre in genres:
            movie1.add_genre(genre)
        assert (movie6 == Movie("as", None)) == True
        assert (movie6.title == "as") == True
        assert movie6.year is None

        with pytest.raises(ValueError):
            movie1.runtime_minutes = -10
        movie1.runtime_minutes = 10
        assert movie1.runtime_minutes == 10
        string1 = "a"
        assert (movie1 == 123) == False
        movie7 = Movie("a", 1900)
        movie8 = Movie("None", None)
        print(movie8.concate())
        assert (movie7 < movie8) == False
        movie1.add_actor("sasa")
        assert (movie1.actors ==[Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")])==True
        movie1.remove_actor(Actor("Auli'i Cravalho"))
        assert (movie1.actors == [Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")])==True
        movie1.remove_actor("asd")
        assert (movie1.actors == [Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")])==True
        movie1.add_actor(Actor("Auli'i Cravalho"))
        assert (movie1.actors ==[Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison"),Actor("Auli'i Cravalho")])==True
        movie1.remove_genre(Genre("asdc"))
        assert (movie1.genres == [Genre("dfg")]) == True
        movie1.add_genre(Genre("asdc"))
        assert (movie1.genres == [Genre("dfg")]) == False
        with pytest.raises(ValueError):
            movie1.runtime_minutes = "sd"
        movie1.actors = ['a','b']







