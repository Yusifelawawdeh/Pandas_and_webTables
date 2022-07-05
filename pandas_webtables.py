# extract tables from wikipedia
from pandas.io.html import read_html
page = 'https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area'

wikitables = read_html(page,  attrs={"class":"wikitable"})

print("Extracted {num} wikitables".format(num=len(wikitables)))

wikitables[0].head()

wikitables[1].shape

wikitables[1]



