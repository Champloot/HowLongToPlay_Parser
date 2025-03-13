import requests
from bs4 import BeautifulSoup
import re

# Vars
game = "dead-cells"
link = f"https://howlongtoplay.ru/games/{game}"

response = requests.get(link)
response_status = response.status_code
text_from_page = response.text
soup = BeautifulSoup(text_from_page, 'lxml')

arr = []

first_block = soup.find('div', class_="game__main-time-item")
second_block = first_block.find_next('div', class_="game__main-time-item")
third_block = second_block.find_next('div', class_="game__main-time-item")

arr = [first_block.text, second_block.text, third_block.text]

# Main campaign
main_campaign = re.findall(r'\d+', arr[0])

# Campaign + additional tasks
campaign_and_add_tasks = re.findall(r'\d+', arr[1])

# Full playthrough
full_playthrough = re.findall(r'\d+', arr[2])

print(main_campaign, campaign_and_add_tasks, full_playthrough)
