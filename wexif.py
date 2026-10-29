import urllib.request
from PIL.ExifTags import TAGS
from PIL import Image
from sys import argv

def main():
	url = argv[1]
	filename = url.split('/')[-1] # выбор названия файла из URL

	if '?' in filename:
		filename = filename.split('?')[0] # обход GET параметров
		
	urllib.request.urlretrieve(url, filename) # загрузка файла в текущую директорию

	img = Image.open(filename)
	exif_data = img.getexif()

	if exif_data:
		print(
			f'Width: {img.size[0]}',
			f'Height: {img.size[1]}',
			f'File Type: {img.format}',
			f'File Name: {img.filename}', sep='\n' # обычные метаданные
		)
		
		for tag_id, data in exif_data.items(): # разделение на имя EXIF тега и его значение
			name = TAGS.get(tag_id, tag_id)
			
			if isinstance(data, bytes): # декодирование значения если оно в байтах
				try:
					data = data.decode()
				except UnicodeDecodeError: # если не получилось декодировать
					data = ''
					
			print(f'{name}: {data}')

if __name__ == '__main__':
	main()
