import webbrowser


class Video():
    """Creates a Video obejcts which holds the title and duration information"""
    
    def __init__(self, title, duration):
        self.title = title;
        self.duration = duration


class Movie(Video):
    """Creates a Movie object, holds Video inforamtion as well as storyline, image, and trailer link"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, mTitle, mStoryline, pImage, tYoutube,duration):
        Video.__init__(self, mTitle, duration)
        self.storyline = mStoryline
        self.poster_image_url = pImage
        self.trailer_youtube_url = tYoutube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):
    """Creats a TvShow Object which holds Video information as well as season and episonde information."""

    def __init__(self, show_title, season, episode, duration):
        Video.__init__(self, showtitle, duration)
        self.seaon = season
