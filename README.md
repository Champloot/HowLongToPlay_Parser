# Игровой Таймер

Этот проект позволяет получать информацию о времени прохождения игр с сайта howlongtoplay.ru. Просто укажите название игры, и программа выведет время для основной кампании, кампании с дополнительными задачами и полного прохождения.

## Установка

1. Склонируйте репозиторий:
      git clone <URL_репозитория>
   cd <папка_проекта>
   

2. Установите необходимые библиотеки:
      pip install requests beautifulsoup4
   

## Использование

Запустите скрипт main.py с указанием названия игры:

python main.py -g "название_игры"


## Пример

python main.py -g "Dead Cells"


## Исключения

Если возникнет ошибка при парсинге данных, программа выведет сообщение "Something went wrong".

## Лицензия

Этот проект является образовательным и не предназначен для коммерческого использования.
