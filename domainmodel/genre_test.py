from domainmodel.genre import Genre


class TestDirectorMethods:

    def test_init(self):
        genre1 = Genre("Taika Waititi")
        assert repr(genre1) == "<Genre Taika Waititi>"
        genre2 = Genre("")
        assert genre2.genre_name is None
        genre3 = Genre(3)
        assert genre3.genre_name is None
        genre1.genre_name = "josie"
        assert genre1.genre_name == "josie"
        assert (genre1.genre_name == genre2.genre_name)== False
        genre1 = Genre("Horror")
        assert repr(genre1) == "<Genre Horror>"

