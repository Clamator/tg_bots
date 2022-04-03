import requests
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/all/'
news_lst = []
print(news_lst)
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')
main_table = soup.find('div', class_='tm-articles-subpage').find('div', class_='tm-articles-list').find_all('article', class_='tm-articles-list__item')
first_new = main_table[0].find('h2', class_='tm-article-snippet__title tm-article-snippet__title_h2').find('a').get('href')
news_lst.append(first_new)
print(news_lst)