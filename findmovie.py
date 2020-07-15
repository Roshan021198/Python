# Find Releasd Year Of movie
from imdby.imdb import imdb

# creating instance of imdb
ia = imdb.imdby()

# getting the movei with name
moviename = input("Enter the name: ")
search = ia.search_movie("moviename")

# getting movie year
year = search[0]['year']

# Printing movie name and year
print(search[0]['title'] + " : " + str(year))
