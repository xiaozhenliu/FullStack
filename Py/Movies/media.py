import webbrowser

class Movie():
    def __init__(self,title,storyline,poster_image,trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def play_trailer(self):
        webbrowser.open_new(self.trailer_youtube_url)
