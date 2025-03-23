from http.client import responses

from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import re
from requests_html import HTMLSession


class DefaultError(Exception):
    pass


header = {'user-agent': UserAgent().chrome}


def parse(game_code: int = 45727) -> list:
    link = f"https://howlongtobeat.com/game/{game_code}"

    response = requests.get(link, headers=header)
    if response.status_code != 200:
        raise DefaultError("Error")
    text_from_page = response.text
    soup = BeautifulSoup(text_from_page, 'html.parser')
    blocks = soup.find_all('li', class_="GameStats_short__tSJ6I time_100")
    # print(blocks)
    info_from_blocks = [i.text for i in blocks]
    ans = []
    for time in info_from_blocks[:-1]:
        current_time = re.findall(r'\d+½?', time)[0].replace('½', '.5')
        ans.append(current_time)
    return ans


def prepare_to_parse(key_word: str = 'Dead cells') -> int:
    # link = "https://howlongtobeat.com/?q=Dark"
    link = "https://howlongtobeat.com/api/ouch/78952b080bf5c22b"
    params = {"searchTerms": ["Dark"]}
    data = {"searchType":"games","searchTerms":["Dark"],"searchPage":2,"size":20,"searchOptions":{"games":{"userId":610615,"platform":"","sortCategory":"popular","rangeCategory":"main","rangeTime":{"min":"null","max":"null"},"gameplay":{"perspective":"","flow":"","genre":"","difficulty":""},"rangeYear":{"min":"","max":""},"modifier":""},"users":{"sortCategory":"postcount"},"lists":{"sortCategory":"follows"},"filter":"","sort":0,"randomizer":0},"useCache":"false"}

    response = requests.post(link)#, data=data, headers=header)
    print(response.text)

    # sesion = requests.session()
    # sesion.headers["User-Agent"] = UserAgent().random
    # rs = sesion.get(link, params=params)
    # soup = BeautifulSoup(rs.text, 'html.parser')
    # blocks = soup.find_all('li', class_="back_darkish GameCard_search_list__IuMbi")
    # print([i.text for i in blocks])

    # s = HTMLSession()
    # res = s.get(link, headers=header)
    # res.html.render(sleep=2, scrolldown=True)
    # soup = BeautifulSoup(res.text, 'html.parser')
    # blocks = soup.find_all('li', class_="back_darkish GameCard_search_list__IuMbi")
    # print([i.text for i in blocks])

    # for _ in range(5):
    #     blocks.append(blocks[-1].find_next('li', class_="back_darkish GameCard_search_list__IuMbi"))
    # print(blocks)

prepare_to_parse('dark')
# print(parse(160592))