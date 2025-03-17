# HowLongToPlay Parser (Pet Project)

Простой скрипт для получения времени прохождения игр с howlongtoplay.ru.

## Требования

*   Python 3.6+
*   `requests`: `pip install requests`
*   `beautifulsoup4`: `pip install beautifulsoup4`

## Запуск

```bash
python main.py -g "Название Игры"

markdown
Пример: python main.py -g "Dead Cells"

Вывод
Выводит время прохождения (ч. м.) для:

Основной кампании
Кампании + доп. задания
Полного прохождения
Ошибки
Если не нашел игру, выведет “Something went wrong”.

Важно
Не делайте слишком много запросов подряд! Уважайте сайт. “`
