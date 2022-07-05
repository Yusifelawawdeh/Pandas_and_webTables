# extract several tables from wikipedia from a single page
from pandas.io.html import read_html
page = 'https://en.wikipedia.org/wiki/New_York_City'

wikitables = read_html(page, index_col=0, attrs={"class":"wikitable"}, header=None)

print ("Extracted {num} wikitables".format(num=len(wikitables)))