import os
from time import sleep
from bs4 import BeautifulSoup
import requests
import pandas as pd

IMAGE_DIR = './images/'

with open('image_data.html', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'lxml')

image_tags = soup.select('.sw-ThumbnailGrid__row > .sw-Thumbnail.sw-Thumbnail--tile')


d_list = []
for i, image_tag in enumerate(image_tags, start=1):
    file_name = f'abs_image_{i}'
    raw_url = image_tag.select_one('a.sw-ThumbnailGrid__details').get('href')
    yahoo_image_url = image_tag.select_one('figure > a:first-of-type > img').get('src')
    print('='*30, i, '='*30)
    print(file_name)
    print(raw_url)
    print(yahoo_image_url)

    d = {
        'file_name': file_name,
        'raw_url': raw_url,
        'yahoo_image_url': yahoo_image_url
    }

    d_list.append(d)
    


df = pd.DataFrame(d_list)
df.to_csv('abs_image_urls.csv', index=None, encoding='utf-8-sig')


df = pd.read_csv('abs_image_urls.csv')

# imageファイルの作成
os.makedirs(IMAGE_DIR)

for file_name, yahoo_image_url in zip(df.file_name, df.yahoo_image_url):
    image = requests.get(yahoo_image_url)
    with open(IMAGE_DIR + file_name + '.jpg', 'wb') as f:
        f.write(image.content)

    sleep(3)