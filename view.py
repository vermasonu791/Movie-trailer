import fresh_tomatoes
import movie

'''here we create a instance of class which is used to pass the data
to Film() class.
'''
rmpag_stry = movie.Film("Rampage story", "something new", "1.jpg", "https://" +
                        "www.youtube.com/watch?v=coOKvrsmQiI")
terminator = movie.Film("Terminator", "fight", "2.jpg", "https://" +
                        "www.youtube.com/watch?v=bx68osizz6w")
pari = movie.Film("Pari", "haunted", "3.jpg", "https://www.youtube.com/" +
                  "watch?v=PQKu78NnyvU")
newyork = movie.Film("Welcome to newyork", "welcome", "4.jpg", "https://" +
                     "www.youtube.com/watch?v=4dCJgNzgs3c")
veery = movie.Film("Veery", "veery ki wedding", "5.jpg", "https://" +
                   "www.youtube.com/watch?v=ytsHyHD_vWs")
aiyaary = movie.Film("Aiyaary", "flag", "6.jpg", "https://www.youtube.com/" +
                     "watch?v=KcWXKmnZZVo")
'''creating a list of all the instances.'''

movies = [rmpag_stry, terminator, pari, newyork, veery, aiyaary]
'''here fresh_tomatoes is module or file and inside the file
we create a open_movies_page() function and we pass the movies list to
this function.
'''
fresh_tomatoes.open_movies_page(movies)
