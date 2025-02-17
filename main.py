import requests



game = "dead-cells"
link = f"https://cubiq.ru/gametime/{game}"
response = requests.get(link)
response_status = response.status_code
text_from_page = response.text
