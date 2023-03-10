import requests
from bs4 import BeautifulSoup 
import csv

url = 'https://limon.kg/ru'
response = requests.get(url)
bs = BeautifulSoup(response.text, 'lxml')

temp = bs.find('div', class_ = 'data-v-2974b40b')
print(temp)


