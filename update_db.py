# -*- coding: utf-8 -*-
import imdb 
from tpb import TPB
from tpb import CATEGORIES, ORDERS
import inspect
import re
import sqlite3
movies = []
ia = imdb.IMDb() 
t = TPB('http://thepiratebay.org') 
counter=0
for i in t.top().category(CATEGORIES.VIDEO.MOVIES):
    # Make TPB titles nice and searchable
    nicestring = re.split(r'\d{4}',i.title)[0][:-1].replace('.',' ')

    imdbmovie = ia.search_movie(nicestring)[0]
    ia.update(imdbmovie)

    movie_rating = "none"
    if  imdbmovie.has_key('rating'):
        movie_rating=imdbmovie['rating']

    movie_title = "unknown"
    if imdbmovie.has_key('long imdb canonical title'):
        movie_title=imdbmovie['long imdb canonical title'] 

    listing = dict(title=movie_title,rating=movie_rating,magnet=i.magnet_link,tpbtitle=i.title)
    print("updating db with: " +str(listing))
    movies.append(listing) 
    counter = 1+counter
    print counter

print('connecting')
conn = sqlite3.connect('webfrontend/wsgi/db.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS movies(title TEXT,rating STRING,magnet STRING,tpbtitle STRING)")
cur.execute("DELETE FROM movies")
print("truncated")
for listing in movies:
    cur.execute("INSERT INTO movies VALUES(?,?,?,?)", [listing['title'], listing['rating'], listing['magnet'], listing['tpbtitle']])
conn.commit()
conn.close()
