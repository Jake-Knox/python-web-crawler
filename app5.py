from imdb import Cinemagoer

ia = Cinemagoer()
# https://cinemagoer.github.io/

# the_matrix = ia.get_movie('0133093')
# for director in the_matrix['directors']:
#     print(director['name'])
# for genre in the_matrix['genres']:
#     print(genre)

# search for a person name
# people = ia.search_person('Mel Brooks')
# for person in people:
#    print(person.personID, person['name'])

# movies = ia.search_movie('western')
# print(movies[0])
# print(movies)
movies = ia.search_movie("The Big Lebowski")
print(movies[0].data)

# Open the text file in read mode
with open('watchlist.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Process the line
        line = line.strip()
        # print(line)
        # movies = ia.search_movie(line)
        # for movie in movies:
        #     print(movie['id'])

        movie = movies[0]
        # movie = ia.get_movie(movie)
        print(movie)
        print(movie.data['year'])       
        for genre in movie['genres']:
            print(genre)



# movies = ia.get_keyword("fantasy")
# print(len(movies))
# for movie in movies:
#     print(movie)


