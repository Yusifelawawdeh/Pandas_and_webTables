from pandas.io.html import read_html
page = 'https://hcad.org/quick-search/'
infoboxes = read_html(page, index_col=0, attrs={"class":"bgcolor_1"})

infoboxes[0].head(10)