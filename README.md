# How Long To Play (HLTP) CLI

Простая утилита для получения информации о времени прохождения игр с сайта HowLongToPlay.ru.


## Использование

1.  **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

2.  **Запустите скрипт, указав название игры через параметр `-g` или `--game`:**

    ```bash
    python main.py -g "Dead Cells"
    ```

    Или:

    ```bash
    python main.py --game "dead-cells"
    ```

    Название игры можно указывать с разными регистрами.


## Пример вывода

`Main campaign: 14h. 59m.`

`Campaign + additional tasks: 27h. 48m.`

`Full playthrough: 64h. 49m.`


## Ошибки

В случае проблем с подключением к сайту или отсутствием информации об игре, будет выведено сообщение "Something went wrong".
