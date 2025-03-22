import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re


class DefaultError(Exception):
    pass


def parse(game_code: int = 45727) -> list:
    header = {'user-agent': UserAgent().random}
    link = f"https://howlongtobeat.com/game/{game_code}"
    response = requests.get(link, headers=header)

    if response.status_code != 200:
        raise DefaultError("Error")

    text_from_page = response.text
    soup = BeautifulSoup(text_from_page, 'html.parser')

    blocks = soup.find_all('li', class_="GameStats_short__tSJ6I time_100")
    info_from_blocks = [i.text for i in blocks]

    for time in info_from_blocks:
        current_time = re.findall(r'\d+', time)
        print(current_time)

def prepare_to_parse(key_word: str = 'Dead cells') -> int:
    pass


parse()
