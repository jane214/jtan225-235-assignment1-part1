from datetime import datetime

from domainmodel.movie import Movie


class Review:
    def __init__(self, movie1: Movie, text, rating_number):
        if movie1 == "" or type(movie1) is not Movie:
            self.__movie = None
        else:
            self.__movie = movie1
        if text == "" or type(text) is not str:
            self.__review_text = None
        else:
            self.__review_text = text
        if type(rating_number) is not int or rating_number < 1 or rating_number > 10:
            self.__rating_number = None
        else:
            self.__rating_number = rating_number
        self.__timestamp = datetime.today()

    @property
    def movie(self):
        return self.__movie

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating_number

    @property
    def timestamp(self):
        return self.__timestamp

    def __repr__(self):
        return f"<Review: {self.__movie} Time: {self.__timestamp}>"

    def __eq__(self, other):
        if not (isinstance(other, Review)):
            return False
        else:
            return (self.__movie == other.__movie and
                    self.__review_text == other.__review_text and
                    self.__rating_number == other.__rating_number and
                    self.__timestamp == other.__timestamp)


# movie = Movie("Moana", 2016)
# review_text = "This movie was very enjoyable."
# rating = 8
# review = Review(movie, review_text, rating)
#
#
# movie3 = Movie("Moana", 2016)
# review_text3 = "This movie was very enjoyable."
# rating3 = 8
# review3 = Review(movie3, review_text3, rating3)
#
#
# movie2 = Movie("asb", 1300)
# review_text2 =""
# rating2 = "sd"
# review2 = Review(movie2,review_text2, rating2)
#
# a = "232"
# print(review.movie)
# print("Review: {}".format(review.review_text))
# print("Rating: {}".format(review.rating))
#
# print(review2.movie)
# print("Review: {}".format(review2.review_text))
# print("Rating: {}".format(review2.rating))
#
# print(review == a)
#
# print(review.timestamp)