# -*- coding: utf-8 -*-
""" Creating the list of favorite movies

This module has only one function main() that:
    - Creates the instances of the class movie, with the information about the
    movies;
    - Create a list with all the instances of the movies;
    - Call the function open_movies_page of the module fresh_tomatoes, and pass
    the list of movies as a parameter. This function will create the html file
    and open it in a web browser.
"""

import media
import fresh_tomatoes


def main():
    """ Creates the list of movies, generates an html file and open it."""

    # Creating the movie No Country for Old Man
    no_country = media.Movie("No Country for Old men", "2007")
    no_country.set_poster_image(
        "https://upload.wikimedia.org/wikipedia/en/8/8b/"
        "No_Country_for_Old_Men_poster.jpg"
    )
    no_country.set_wikipedia(
        "https://en.wikipedia.org/wiki/No_Country_for_Old_Men_(film)"
    )
    no_country.set_rotten_tomatoes(
        "https://www.rottentomatoes.com/m/no_country_for_old_men"
    )
    no_country.set_imdb("https://www.imdb.com/title/tt0477348/")
    no_country.set_trailer_youtube(
        "https://www.youtube.com/watch?v=38A__WT3-o0"
    )

    # Creating the movie The Hateful Eight
    the_hateful_eight = media.Movie("The Hateful Eight", "2015")
    the_hateful_eight.set_poster_image(
        "https://upload.wikimedia.org/wikipedia/en/d/d4/The_Hateful_Eight.jpg"
    )
    the_hateful_eight.set_wikipedia(
        "https://en.wikipedia.org/wiki/The_Hateful_Eight"
    )
    the_hateful_eight.set_rotten_tomatoes(
        "https://www.rottentomatoes.com/m/the_hateful_eight"
    )
    the_hateful_eight.set_imdb("https://www.imdb.com/title/tt3460252/")
    the_hateful_eight.set_trailer_youtube(
        "https://www.youtube.com/watch?v=nIOmotayDMY"
    )

    # Creating the instance of the movie The Devil's Rejects
    the_devils_rejects = media.Movie("The Devil's Rejects", "2005")
    the_devils_rejects.set_poster_image(
        "https://upload.wikimedia.org/wikipedia/en/d/d6/"
        "Devils_rejects_ver2.jpg"
    )
    the_devils_rejects.set_wikipedia(
        "https://en.wikipedia.org/wiki/The_Devil%27s_Rejects"
    )
    the_devils_rejects.set_rotten_tomatoes(
        "https://www.rottentomatoes.com/m/devils_rejects"
    )
    the_devils_rejects.set_imdb("https://www.imdb.com/title/tt0395584/")
    the_devils_rejects.set_trailer_youtube(
        "https://www.youtube.com/watch?v=qrSSKU1416Y"
    )

    # Creating the instance of the movie We Need to Talk About Kevin
    talk_about_kevin = media.Movie("We Need to Talk About Kevin", "2011")
    talk_about_kevin.set_poster_image(
        "https://upload.wikimedia.org/wikipedia/en/f/f6/"
        "We_need_to_talk_about_kevin_ver2.jpg"
    )
    talk_about_kevin.set_wikipedia(
        "https://en.wikipedia.org/wiki/We_Need_to_Talk_About_Kevin_(film)"
    )
    talk_about_kevin.set_rotten_tomatoes(
        "https://www.rottentomatoes.com/m/we_need_to_talk_about_kevin"
    )
    talk_about_kevin.set_imdb("https://www.imdb.com/title/tt1242460/")
    talk_about_kevin.set_trailer_youtube(
        "https://www.youtube.com/watch?v=Mmf42pkfgZw"
    )

    # Creating the instance of the movie Raw
    raw = media.Movie("Raw", "2016")
    raw.set_poster_image(
        "https://upload.wikimedia.org/wikipedia/en/d/d2/Raw_(film).png"
    )
    raw.set_wikipedia("https://en.wikipedia.org/wiki/Raw_(film)")
    raw.set_rotten_tomatoes("https://www.rottentomatoes.com/m/raw_2017")
    raw.set_imdb("https://www.imdb.com/title/tt4954522/")
    raw.set_trailer_youtube("https://www.youtube.com/watch?v=gFlXVX2af_Y")

    # Creating the instance of the movie The House That Jack Built
    house_jack_built = media.Movie("The House That Jack Built", "2018")
    house_jack_built.set_poster_image(
        "https://upload.wikimedia.org/wikipedia/en/4/4c/"
        "The_House_That_Jack_Built.png"
    )
    house_jack_built.set_wikipedia(
        "https://en.wikipedia.org/wiki/The_House_That_Jack_Built_(2018_film)"
    )
    house_jack_built.set_rotten_tomatoes(
        "https://www.rottentomatoes.com/m/the_house_that_jack_built_2018"
    )
    house_jack_built.set_imdb("https://www.imdb.com/title/tt4003440/")
    house_jack_built.set_trailer_youtube(
        "https://www.youtube.com/watch?v=BYF2tfdD1fA"
    )

    # Create a list with all instances of movies
    movies = [
        no_country,
        the_hateful_eight,
        the_devils_rejects,
        talk_about_kevin,
        raw,
        house_jack_built
    ]

    # Make the site with the movies in the list
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
