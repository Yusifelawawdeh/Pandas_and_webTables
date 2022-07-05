import pandas as pd

airports = pd.read_html('https://en.wikipedia.org/wiki/List_of_international_airports_by_country')

length = len(airports)
print(length)

print(airports[0])