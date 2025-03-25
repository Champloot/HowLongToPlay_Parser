from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import re


class DefaultError(Exception):
    pass


def parse(game_code: int = 45727, target: str = None) -> list:
    link = f"https://howlongtobeat.com/game/{game_code}"

    header = {'user-agent': UserAgent().chrome}
    response = requests.get(link, headers=header)
    if response.status_code != 200:
        raise DefaultError("Error")
    text_from_page = response.text
    soup = BeautifulSoup(text_from_page, 'html.parser')
    name = soup.find('div', class_="GameHeader_profile_header__q_PID shadow_text").text
    if target == 'name':
        return [name]
    blocks = soup.find_all('li', class_="GameStats_short__tSJ6I time_100")
    info_from_blocks = [i.text for i in blocks]
    ans = [name]
    for time in info_from_blocks[:-1]:
        current_time = re.findall(r'\d+½?', time)[0].replace('½', '.5')
        ans.append(current_time)
    return ans
