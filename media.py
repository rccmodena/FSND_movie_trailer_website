# -*- coding: utf-8 -*-
""" Module Class Movie

This module defines the class Movie, that provides a way to store movie related
information.
"""


class Movie:
    """
    A class that provides a way to store movie related information.

    Attributes:
    -----------
    title : str
        the title of the movie
    year : str
        the year of the movie
    poster_image : str, optional
        the url to the image of the poster the movie (default is the path to an
        image with the sentence comming soon)
    wikipedia : str, optional
        the url to wikipedia
    rotten_tomatoes : str, optional
        the url to Rotten Tomatoes
    imdb : str, optional
        the url to IMDb
    trailer_youtube : str, optional
        the youtube url to the youtube trailer of the movie

    Methods:
    --------
    get_title()
        provides the title of the movie
    set_title(title)
        set the title of the movie
    get_year()
        provides the year of the movie
    set_year(year)
        set the year of the movie
    get_poster_image()
        provides the poster image url of the movie
    set_poster_image(poster_image)
        set the poster image url of the movie
    get_wikipedia()
        provides the wikipedia url of the movie
    set_wikipedia(wikipedia):
        set the wikipedia url of the movie
    get_rotten_tomatoes()
        provides the rotten tomatoes url of the movie
    set_rotten_tomatoes(rotten_tomatoes)
        set the rotten tomatoes url of the movie
    get_imdb()
        provides the IMDb url of the movie
    set_imdb(imdb)
        set the IMDb url of the movie
    get_trailer_youtube()
        provides the youtube url of the movie
    set_trailer_youtube(trailer_youtube)
        set the youtube url of the movie
    """

    def __init__(self, movie_title, movie_year):
        """
        Parameters:
        -----------
        title : str
            the title of the movie
        year : str
            the year of the movie
        """

        self.title = movie_title
        self.year = movie_year
        self.poster_image = (
            "https://cdn.pixabay.com/photo/2017/02/16/02/54/"
            "coming-soon-2070393_960_720.jpg"
        )
        self.wikipedia = "#"
        self.rotten_tomatoes = "#"
        self.imdb = "#"
        self.trailer_youtube = "#"

    def get_title(self):
        """
        Provides the title of the movie.

        Returns:
        --------
        str
            the title of the movie
        """

        return self.title

    def set_title(self, title):
        """
        Set the title of the movie.

        Parameters:
        -----------
        title : str
            the title of the movie
        """

        self.title = title

    def get_year(self):
        """
        Provides the year of the movie.

        Returns:
        --------
        str
            the year of the movie
        """

        return self.year

    def set_year(self, year):
        """
        Set the year of the movie.

        Parameters:
        -----------
        year : str
            the year of the movie
        """

        self.title = year

    def get_poster_image(self):
        """
        Provides the poster image url of the movie.

        Returns:
        --------
        str
            the poster image url of the movie
        """

        return self.poster_image

    def set_poster_image(self, poster_image):
        """
        Set the poster image url of the movie

        Parameters:
        -----------
        poster_image : str
            the poster image url of the movie
        """

        self.poster_image = poster_image

    def get_wikipedia(self):
        """
        Provides the wikipedia url of the movie.

        Returns:
        --------
        str
            the wikipedia url of the movie
        """

        return self.wikipedia

    def set_wikipedia(self, wikipedia):
        """
        Set the wikipedia url of the movie

        Parameters:
        -----------
        wikipedia : str
            the wikipedia url of the movie
        """

        self.wikipedia = wikipedia

    def get_rotten_tomatoes(self):
        """
        Provides the rotten tomatoes url of the movie.

        Returns:
        --------
        str
            the rotten tomatoes url of the movie
        """

        return self.rotten_tomatoes

    def set_rotten_tomatoes(self, rotten_tomatoes):
        """
        Set the rotten tomatoes url of the movie

        Parameters:
        -----------
        rotten_tomatoes : str
            the rotten tomatoes url of the movie
        """

        self.rotten_tomatoes = rotten_tomatoes

    def get_imdb(self):
        """
        Provides the IMDb url of the movie.

        Returns:
        --------
        str
            the IMDb url of the movie
        """

        return self.imdb

    def set_imdb(self, imdb):
        """
        Set the IMDb url of the movie

        Parameters:
        -----------
        imdb : str
            the IMDb url of the movie
        """

        self.imdb = imdb

    def get_trailer_youtube(self):
        """
        Provides the youtube url of the movie.

        Returns:
        --------
        str
            the youtube url of the movie
        """

        return self.trailer_youtube

    def set_trailer_youtube(self, trailer_youtube):
        """
        Set the youtube url of the movie

        Parameters:
        -----------
        trailer_youtube : str
            the youtube url of the movie
        """

        self.trailer_youtube = trailer_youtube
