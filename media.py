__author__ = 'Mayer'


class Movie(object):
    def __init__(self, title, image, trailer_url):
        self.title = title
        self.poster_image_url = image
        self.trailer_youtube_url = trailer_url

