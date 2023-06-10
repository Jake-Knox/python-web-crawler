from imdb import Cinemagoer
# pip install cinemagoer

# In this file:
# trying to extract film data from letterboxd.com
# result...
# theres a new version which i'll move on to

# https://imdbpy.readthedocs.io/en/latest/usage/data-interface.html


# create an instance of the Cinemagoer class
ia = Cinemagoer()

# get a movie
movie = ia.get_movie('0133093')
# movie = ia.get_movie('0133093', info=['taglines', 'plot'])

# print the names of the directors of the movie
print('Directors:')
for director in movie['directors']:
    print(director['name'])

# print the genres of the movie
print('Genres:')
for genre in movie['genres']:
    print(genre)


print("---")

movies = ia.search_movie('matrix')
movie = movies[0]
print(movie)
print(movie.current_info)
ia.update(movie, info=["plot"])
print(movie.current_info)



# search for a person name
# people = ia.search_person('Mel Gibson')
# for person in people:
#    print(person.personID, person['name'])


