from pandas.io.html import read_html
page = 'https://hcad.org/quick-search/'
infoboxes = read_html(page, index_col=0, attrs={"class":"bgcolor_1"})

file_name = './my_file.csv'
infoboxes[0].to_csv(file_name, sep='\t')
