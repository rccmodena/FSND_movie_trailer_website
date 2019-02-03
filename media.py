# -*- coding: utf-8 -*-
""" This module creates the class Movie """


class Movie():
    """ This class provides a way to store movie related information """

    # Wikipedia Posters URL
    POSTER_WIKI_URL = ""

    # Wikipedia URL
    WIKI_URL = ""

    # Rotten Tomatoes URL
    ROTTEN_TOMATOES_URL = ""

    # Imdb URL
    IMDB_URL = ""

    # Youtube URL
    YOUTUBE_URL = ""

    def __init__(self, movie_title, movie_year):
        """ Constructor of the class Movie """

        # The title of the movie
        self.title = movie_title

        # The year of the movie
        self.year = movie_year

        # The url to the image of the poster the movie
        self.poster_image = (
            "https://cdn.pixabay.com/photo/2017/02/16/02/54/"
            "coming-soon-2070393_960_720.jpg"
        )

        # The url to wikipedia
        self.wikipedia = "#"

        # The url to Roten Tomatoes
        self.rotten_tomatoes = "#"

        # The url to IMDb
        self.imdb = "#"

        # The youtube url to the trailer of the movie
        self.trailer_youtube = "#"

    def get_title(self):
        """ Get the title of the movie """
        return self.title

    def set_title(self, title):
        """ Set the title of the movie """
        self.title = title

    def get_year(self):
        """ Get the year of the movie """
        return self.year

    def set_year(self, year):
        """ Set the year of the movie """
        self.title = year

    def get_poster_image(self):
        """ Get the poster image url of the movie """
        return self.poster_image

    def set_poster_image(self, poster_image):
        """ Set the poster image url of the movie """
        self.poster_image = self.POSTER_WIKI_URL + poster_image

    def get_wikipedia(self):
        """ Get the wikipedia url of the movie """
        return self.wikipedia

    def set_wikipedia(self, wikipedia):
        """ Set the wikipedia url of the movie """
        self.wikipedia = self.WIKI_URL + wikipedia

    def get_rotten_tomatoes(self):
        """ Get the rotten tomatoes url of the movie """
        return self.rotten_tomatoes

    def set_rotten_tomatoes(self, rotten_tomatoes):
        """ Set the rotten tomatoes url of the movie """
        self.rotten_tomatoes = self.ROTTEN_TOMATOES_URL + rotten_tomatoes

    def get_imdb(self):
        """ Get the IMDb url of the movie """
        return self.imdb

    def set_imdb(self, imdb):
        """ Set the IMDb url of the movie """
        self.imdb = self.IMDB_URL + imdb

    def get_trailer_youtube(self):
        """ Get the youtube url of the movie """
        return self.trailer_youtube

    def set_trailer_youtube(self, trailer_youtube):
        """ Set the youtube url of the movie """
        self.trailer_youtube = self.YOUTUBE_URL + trailer_youtube
