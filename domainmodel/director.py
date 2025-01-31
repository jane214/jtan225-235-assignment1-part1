"""
    @director_full_name.setter
    def director_full_name(self, value):
        if value == "" or type(value) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = value.strip()
"""
import pytest


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
        return f"<Director {self.director_full_name}>"

    def __eq__(self, other):
        if not (isinstance(other, Director) or other.director_full_name is None):
            return False
        else:
            return self.director_full_name == other.director_full_name

    def __lt__(self, other):
        return self.director_full_name < other.director_full_name

    def __hash__(self):
        return hash(self.director_full_name)


# class TestDirectorMethods:
#
#     def test_init(self):
#         director1 = Director("Taika Waititi")
#         assert repr(director1) == "<Director Taika Waititi>"
#         director2 = Director("")
#         assert director2.director_full_name is None
#         director3 = Director(3)
#         assert director3.director_full_name is None
#
# # test_init();
