import requests

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
filename = 'data/raw/iris.csv'

with open(filename, 'wb') as ofile:
   response = requests.get(url)
   file.write(response.content)