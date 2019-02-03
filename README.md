# Project: Movie Trailer Website

This is the first project of the Udacity's Full Stack Web Developers Nanodegree.

The project consists in write server-side code to store a list of your favorite movies, including box art imagery, links to external websites and a movie trailer URL. The code will generate a static web page allowing visitors to browse their movies and watch the trailers.

This project was forked from [ud036_StarterCode](https://github.com/udacity/ud036_StarterCode).

## Install

To install this project there are two ways:
- Download the repository ZIP file and unpack it.
- Or clone the repository

```sh
$ git clone https://github.com/rccmodena/movie_trailer_website.git
$ cd movie_trailer_website/
```

## Creating the list of your favorite movies

The project has three main files:
- `media.py`
- `entertainment_center.py`
- `fresh_tomatoes.py`

To create your list of favorite movies, you only need to alter the `entertainment_center.py` file.

To include one movie, the minimum information is the movie title and it's year.

```
movie_a = media.Movie("Movie A Title", "2019")
```

Optionally, you can add four more information to a movie:
- Link to the movie poster;

```
movie_a.set_poster_image("https://upload.wikimedia.org/movie_a.jpg")
```

- Link to the Youtube trailer;

```
movie_a.set_trailer_youtube("https://www.youtube.com/movie_a")
```

- Link to the Wikipedia page;

```
movie_a.set_wikipedia("https://en.wikipedia.org/wiki/movie_a")
```

- Link to the Rotten Tomatoes page;

```
movie_a.set_rotten_tomatoes("https://www.rottentomatoes.com/movie_a")
```

- Link to IMDb;

```
movie_a.set_imdb("https://www.imdb.com/title/movie_a")
```


Don't forget to create a list of your movies:

```
movies = [
      movie_a,
      movie_b
  ]
```

And, call the function `open_movies_page` with the list as argument.

```
fresh_tomatoes.open_movies_page(movies)
```

## Generating the website

After creating your list of movies in the `entertainment_center.py`, you'll only need to enter in the folder of the project and run this command:

```
$ python entertainment_center.py
```

The program will automatically open the website in the browser (in a new tab, if possible).

## Requirements

This project was implemented with **Python 3.7.2**, and tested on **Mozilla Firefox 65.0 (Quantum)**.

Only Python Standard Libraries were used:
- [webbrowser](https://docs.python.org/3.7/library/webbrowser.html)
- [os](https://docs.python.org/3.7/library/os.html)
- [re](https://docs.python.org/3.7/library/re.html)

The website uses:
- [Bootstrap 4.2.1](https://getbootstrap.com/docs/4.2/getting-started/introduction/)
- [Popper.js 1.14.6](https://popper.js.org/)
- [jQuery 3.3.1](https://code.jquery.com/)

## How to Contribute

If you find any bug or have a suggestion for another resources, feel free to improve this project.

First, you have to fork this repository.

Next, clone this repository to your computer to make the changes.

Once you've pushed changes to your local repository, you can issue a pull request.

## License

The contents of this repository are covered under the [MIT License](LICENSE).
