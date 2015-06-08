__author__ = 'Mayer'


class Movie(object):
    def __init__(self, title, image, trailer_url, storyline):
        """
        :param title:
        :param image:
        :param trailer_url:
        :param storyline:
        :return: a Movie object which contains above info
        """
        self.title = title
        self.poster_image_url = image
        self.trailer_youtube_url = trailer_url
        self.storyline = storyline

