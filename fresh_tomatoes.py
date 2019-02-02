import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Project: Movie Trailer Website!</title>

    <!-- Bootstrap 4 -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>

    <style media="screen">
        main {
            padding-top: 30px;
        }
        .movie-card {
            padding: 20px;
        }
        .movie-card:hover {
            background-color: #b1bfa6;
            cursor: pointer;
        }
        .modal-title{
            font-weight: bold;
        }
    </style>

    <script>
        // Open the modal with movie information when clicking on the movie cards
        $(document).on('click', '.movie-card', function (event) {

            // Gather the information about the movie
            var movie_title = $(this).attr('data-movie-title')
            var movie_year = $(this).attr('data-movie-year')
            var movie_wikipedia = $(this).attr('data-wikipedia')
            var movie_rotten_tomatoes = $(this).attr('data-rotten-tomatoes')
            var movie_imdb = $(this).attr('data-imdb')

            //Open the modal with the movie details
            $('#ModalMoviedetails').modal('toggle')

            //Display the correct movie title and year
            $('#ModalMoviedetailsTitle').text(movie_title + ' ('+movie_year+')')

            //Add the correct path to wikipedia page of the movie
            //If the wikipedia page was not informed, set the attribute onClick empty
            if (movie_wikipedia != "#"){
                $('#id_wikipedia').attr('onClick', "window.open('"+movie_wikipedia+"', '_blank');")
            } else {
                $('#id_wikipedia').attr('onClick', '');
            }

            //Add the correct path to rotten tomatoes page of the movie
            //If the rotten tomatoes page was not informed, set the attribute onClick empty
            if (movie_rotten_tomatoes != "#"){
                $('#id_rotten_tomatoes').attr('onClick', "window.open('"+movie_rotten_tomatoes+"', '_blank');")
            } else {
                $('#id_rotten_tomatoes').attr('onClick', '');
            }

            //Add the correct path to imbdb page of the movie
            //If the imdb page was not informed, set the attribute onClick empty
            if (movie_imdb != "#"){
                $('#id_imdb').attr('onClick', "window.open('"+movie_imdb+"', '_blank');")
            } else {
                $('#id_imdb').attr('onClick', '');
            }
        });

        // Animate in the movies when the page loads
        $(document).ready(function () {
            $('.movie-card').hide().first().show("fast", function showNext() {
                $(this).next("div").show("fast", showNext);
            });
        });

    </script>


</head>
'''


# The main page layout and title bar
main_page_content = '''
    <body>

        <header>

            <!-- Navbar -->
            <div class="pos-f-t">
                <nav class="navbar navbar-dark bg-dark">
                    <a class="navbar-brand" href="#">My Favourite Movies</a>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNanodegreeDetails" aria-controls="navbarNanodegreeDetails" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                </nav>
                <div class="collapse" id="navbarNanodegreeDetails">
                    <div class="navbar-nav bg-dark p-4">
                        <h5 class="text-white h5">Project: Movie Trailer Website!</h5>
                        <div class="text-muted">
                            <p>This is the project Movie Trailer Website, part of the Full Stack Web Developer Nanodegree (Udacity).</p>
                            <p><a class="badge badge-info" href="https://github.com/rccmodena/movie_trailer_website" target="_blank">Click here</a> to go to the repository's page.</p>
                        </div>
                    </div>
                </div>
            </div>

        </header>

        <main>

            <!-- Modal with the Movie Information -->
            <div class="modal fade" id="ModalMoviedetails" tabindex="-1" role="dialog" aria-labelledby="ModalMoviedetailsTitle" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="ModalMoviedetailsTitle">Modal title</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            <button type="button" class="btn btn-danger btn-lg btn-block"><strong>Watch the Trailer</strong></button>
                            <button id="id_wikipedia" type="button" class="btn btn-info btn-lg btn-block"><strong>Wikipedia</strong></button>
                            <button id="id_rotten_tomatoes" type="button" class="btn btn-info btn-lg btn-block"><strong>Rotten Tomatoes</strong></button>
                            <button id="id_imdb" type="button" class="btn btn-info btn-lg btn-block"><strong>IMDb</strong></button>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Container with the Movie Cards -->
            <div class="container">
                <div class="row">
                    {movie_cards}
                </div>
            </div>
        </main>
    </body>
</html>
'''



# A single movie entry html template
movie_cards_content = '''
<div class="col-md-6 col-lg-4 movie-card" data-trailer-youtube-id="{trailer_youtube_id}" data-movie-title="{movie_title}" data-movie-year="{movie_year}" data-wikipedia="{movie_wikipedia}" data-rotten-tomatoes="{movie_rotten_tomatoes}" data-imdb="{movie_imdb}">
    <div class="card text-white bg-dark h-100">
        <div class="card-body text-center">
            <img src="{poster_image_url}" alt="{poster_alt}" width="220" height="342">
            <h5>{movie_title}</h5>
            <h5>({movie_year})</h5>
        </div>
    </div>
</div>
'''


def create_movie_cards_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.get_trailer_youtube())
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.get_trailer_youtube())
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_cards_content.format(
            movie_title=movie.get_title(),
            movie_year=movie.get_year(),
            poster_image_url=movie.get_poster_image(),
            poster_alt=movie.get_title()+" Movie Poster.",
            movie_wikipedia=movie.get_wikipedia(),
            movie_rotten_tomatoes=movie.get_rotten_tomatoes(),
            movie_imdb=movie.get_imdb(),
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_cards=create_movie_cards_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
