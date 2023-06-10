import imdb
# pip install imdbpy

# In this file:
# trying to extract film data from letterboxd.com
# result...
# theres a new version which i'll move on to

# Create an instance of the IMDb class
ia = imdb.IMDb()

# Search for movies from the 1920s to 1940s
movies = ia.search_movies(years='1920-1949')

# Extract desired information from the movie objects
for movie in movies:
    title = movie['title']
    directors = movie['directors']
    poster = movie['full-size cover url']

    # Process the extracted data as needed
    print("Title:", title)
    print("Directors:", directors)
    print("Poster:", poster)
    print("------------------")
