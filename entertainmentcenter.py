import media
import fresh_tomatoes

#create media objects of movies to display
wolf_wall_st = media.Movie(
    "The Wolf of Wall st",
    "This is the story of New York stockbroker, Jordan Belfort. From the\
     American dream to corporate greed, Belfort goes from penny stocks and\
     righteousness to IPOs and a life of corruption in the late 80s.",
    "http://t1.gstatic.com/images?q=tbn:ANd9GcTm52BWbxXmwOpfz5rmx0BNBj79kSQoGpYPq4TVt07Jel5En6aC",
    "https://www.youtube.com/watch?v=iszwuX1AK6A", "50")

forrest_gump = media.Movie(
    "Forrest Gump",
    "Forrest Gump is a 1994 American comedy-drama film based on the 1986\
    novel of the same name by Winston Groom.",
    "http://t3.gstatic.com/images?q=tbn:ANd9GcQCFOcMb5_zkdZg4B4JvIGLlTQTvLdtLjiS5axJJDqP1FaI8Yyx",
    "https://www.youtube.com/watch?v=uPIEn0M8su0", "50")

d_wears_p = media.Movie(
    "The Devil Wears Prada",
    "A young intern trys to put up with Merril Streeps crap.",
    "https://upload.wikimedia.org/wikipedia/en/e/e7/The_Devil_Wears_Prada_main_onesheet.jpg",
    "https://www.youtube.com/watch?v=LG0xYJJbko8", "50")

movies = [wolf_wall_st, forrest_gump, d_wears_p]

#send objects and open display page.
fresh_tomatoes.open_movies_page(movies)
