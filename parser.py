import requests
from bs4 import BeautifulSoup

# Vars
game = "dead-cells"
link = f"https://howlongtoplay.ru/games/{game}"

response = requests.get(link)
response_status = response.status_code
text_from_page = response.text
soup = BeautifulSoup(text_from_page, 'lxml')

block = soup.find_all('div', class_="game__main-time-item")

print(block)