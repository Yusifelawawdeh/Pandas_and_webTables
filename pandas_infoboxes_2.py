from pandas.io.html import read_html
page = 'https://en.wikipedia.org/wiki/Lisbon'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox geography vcard"})
wikitables = read_html(page, index_col=0, attrs={"class":"wikitable"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
print ("Extracted {num} wikitables".format(num=len(wikitables)))