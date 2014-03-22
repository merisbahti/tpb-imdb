import imdb 
from tpb import TPB
from tpb import CATEGORIES, ORDERS
import inspect

ia = imdb.IMDb() # by default access the web.
t = TPB('http://thepiratebay.org') # create a TPB object with default domain
count = 0
for i in t.top().category(CATEGORIES.VIDEO.MOVIES):
        print i.title
        print ia.search_movie(i.title.replace('.',' '))[0]['long imdb canonical title']
        count = count + 1
        print("------------------------------------------------------")
        if count > 10:
            break
