# -*- coding: utf-8 -*-
""" This module has only one function main().

    The function main() creates the list of favourite movies and generates an
html file and open it.
"""

import media
import fresh_tomatoes

def main():
    """ Creates the list of favourite movies and generates an html file
    and open it.
    """

    # Creating the movie No Country for Old Man
    no_country = media.Movie("No Country for Old men", "2007")
    no_country.set_poster_image("8/8b/No_Country_for_Old_Men_poster.jpg")
    no_country.set_wikipedia("No_Country_for_Old_Men_(film)")
    no_country.set_rotten_tomatoes("m/no_country_for_old_men")
    no_country.set_imdb("title/tt0477348/")
    no_country.set_trailer_youtube("watch?v=38A__WT3-o0")

    # Creating the movie The Hateful Eight
    the_hateful_eight = media.Movie("The Hateful Eight", "2015")
    the_hateful_eight.set_poster_image("d/d4/The_Hateful_Eight.jpg")
    the_hateful_eight.set_wikipedia("The_Hateful_Eight")
    the_hateful_eight.set_rotten_tomatoes("m/the_hateful_eight")
    the_hateful_eight.set_imdb("title/tt3460252/")
    the_hateful_eight.set_trailer_youtube("watch?v=nIOmotayDMY")

    # Creating the instance of the movie The Devil's Rejects
    the_devils_rejects = media.Movie("The Devil's Rejects", "2005")
    the_devils_rejects.set_poster_image("d/d6/Devils_rejects_ver2.jpg")
    the_devils_rejects.set_wikipedia("The_Devil%27s_Rejects",)
    the_devils_rejects.set_rotten_tomatoes("m/devils_rejects",)
    the_devils_rejects.set_imdb("title/tt0395584/",)
    the_devils_rejects.set_trailer_youtube("watch?v=qrSSKU1416Y")

    # Creating the instance of the movie We Need to Talk About Kevin
    talk_about_kevin = media.Movie("We Need to Talk About Kevin", "2011")
    talk_about_kevin.set_poster_image(
        "f/f6/We_need_to_talk_about_kevin_ver2.jpg"
    )
    talk_about_kevin.set_wikipedia("We_Need_to_Talk_About_Kevin_(film)")
    talk_about_kevin.set_rotten_tomatoes("m/we_need_to_talk_about_kevin")
    talk_about_kevin.set_imdb("title/tt1242460/")
    talk_about_kevin.set_trailer_youtube("watch?v=Mmf42pkfgZw")

    # Creating the instance of the movie Raw
    raw = media.Movie("Raw", "2016")
    raw.set_wikipedia("d/d2/Raw_%28film%29.png")
    raw.set_poster_image("Raw_(film)")
    raw.set_rotten_tomatoes("m/raw_2017")
    raw.set_imdb("title/tt4954522/")
    raw.set_trailer_youtube("watch?v=gFlXVX2af_Y")

    # Creating the instance of the movie The House That Jack Built
    house_jack_built = media.Movie("The House That Jack Built", "2018")
    house_jack_built.set_poster_image("4/4c/The_House_That_Jack_Built.png")
    house_jack_built.set_wikipedia("The_House_That_Jack_Built_(2018_film)")
    house_jack_built.set_rotten_tomatoes("m/the_house_that_jack_built_2018")
    house_jack_built.set_imdb("title/tt4003440/")
    house_jack_built.set_trailer_youtube("watch?v=BYF2tfdD1fA")

    # Create a list with all instances of movies
    movies = [
        no_country,
        the_hateful_eight,
        the_devils_rejects,
        talk_about_kevin,
        raw,
        house_jack_built
    ]

    #Make the site with the movies in the list
    fresh_tomatoes.open_movies_page(movies)

# If executing this module run main() function
if __name__ == '__main__':
    main()
