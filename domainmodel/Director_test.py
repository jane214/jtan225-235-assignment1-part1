import pytest

from domainmodel.director import Director


class TestDirectorMethods:

    def test_init(self):
        director1 = Director("Taika Waititi")
        assert repr(director1) == "<Director Taika Waititi>"
        director2 = Director("")
        assert director2.director_full_name is None
        director3 = Director(3)
        assert director3.director_full_name is None
        director1.director_full_name="josie"
        assert director1.director_full_name=="josie"
        assert (director1 == director3) == True
