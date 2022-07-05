# change the index table
from pandas.io.html import read_html
page = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'

wikitables = read_html(page, index_col=1, attrs={"class":"wikitable"})

print("Extracted {num} wikitables".format(num=len(wikitables)))

