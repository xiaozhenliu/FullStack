import fresh_tomatoes
import media

shawshank = media.Movie("The Shawshank Redemption",
            "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
            "http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX214_AL_.jpg",
            "http://www.imdb.com/video/imdb/vi3877612057?ref_=tt_pv_vi_aiv_1")

movies = [shawshank]
fresh_tomatoes.open_movies_page(movies)
