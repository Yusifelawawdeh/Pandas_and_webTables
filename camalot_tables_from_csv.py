import camelot

tables = camelot.read_pdf('alpha.pdf', pages='1')
print(tables)

tables.export('alpha.csv', f='csv', compress=True)
tables[0].to_csv('alpha.csv')
