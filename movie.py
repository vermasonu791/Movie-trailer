import webbrowser


class Film():
    '''here Film() is a class which is used to intialize
    the methods and variable'''
    def __init__(self, movie_title, movie_stryln, poster_image, trailer_utbe):
        '''__init__() is a special type of function which used to create a
        space in memory and it will store the all the details.
        '''
        self.title = movie_title
        self.storyline = movie_stryln
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_utbe

    def show_trailer(self):
        '''show_trailer() is a function and inside a function
        webbrowser is a module and inside a module open() function
        is used to open a browser link.
        '''
        webbrowser.open(self.trailer_youtube_url)
