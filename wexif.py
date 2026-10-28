import urllib.request
from sh import exiftool
from sys import argv

url = argv[1]
filename = url.split('/')[-1] # выбор названия файла из URL

if '?' in filename:
	filename = filename.split('?')[0] # обход GET параметров

urllib.request.urlretrieve(url, filename)

print(exiftool(filename))
