import imdb

ia = imdb.IMDb()

# https://www.geeksforgeeks.org/python-imdbpy-searching-a-movie/
# look at the bottom for similar reads

# items = ia.search_movie('dollars')
# for i in items:
#     print(i)

# name = "duck soup"
# search = ia.search_movie(name)
# for i in search:
#     print(i)

# name = "The Big Lebowski"
# search = ia.search_movie(name)
# print(search)

# work with year
search = ia.get_movie("0118715")
year = search['year']
print(search['title'] + " : " + str(year))
