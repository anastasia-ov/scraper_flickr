import requests
from time import sleep
from random import randint
from bs4 import BeautifulSoup as BS

URL = 'https://www.flickr.com/search/?text='
QUERY = 'fog+forest'

resp = requests.get(URL+QUERY)

if resp.status_code == 200:
    soup = BS(resp.content, 'html.parser')
    photo = soup.find_all('div', class_='photo-list-photo-view')
    links = []
    for item in photo:
        item = str(item)
        link = item[item.find('background-image')+22:len(item)-47]
        links.append(link)

    for l in links:
        url = 'https:' + l
        sleep(randint(1, 3))
        resp_img = requests.get(url)
        if resp_img.status_code == 200:
            f = open(l[34:], mode='wb')
            f.write(resp_img.content)
            f.close()
        else:
            print('Ошибка: код', resp_img.status_code)
else:
    print('Ошибка: код', resp.status_code)


