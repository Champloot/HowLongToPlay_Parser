import sqlite3


def data_base_main(cmd: str='select', *args):
    db = sqlite3.connect('games.db')

    global curs
    curs = db.cursor()

    match cmd:
        case 'add':
            add_to_game_name_table(*args)
        case 'del':
            del_from_game_name_table(*args)
        case 'select':
            return select_from_game_name_table(*args)
        case '__reCreate':
            create_game_name_table()
        case _:
            pass



    db.commit()
    db.close()


def create_game_name_table():
    # Таблица для корректной подстановки названия игры в поисковую строку.
    # Будет два столбца:
    #     standard_name - то, как назвал бы игру пользователь. Типа "Dead Cells" или "Dark Souls 3";
    #     correct_name - то, как он указывается в поисковике. Типа "dead-cells".

    curs.execute("""
    CREATE TABLE game_names (
        standard_name text,
        correct_name text
    )
    """)

def del_from_game_name_table(standard_name):
    curs.execute(f"DELETE FROM game_names WHERE standard_name=={standard_name}")

def add_to_game_name_table(*args):
    [standard_name, correct_name] = args
    curs.execute(f"INSERT INTO game_names VALUES ('{standard_name}','{correct_name}')")

def select_from_game_name_table(standard_name: str):
    curs.execute(f"SELECT * FROM game_names WHERE standard_name=='{standard_name}'")
    return curs.fetchone()

res = data_base_main('select', 'Dead cells')
if res is None:
    data_base_main('add', 'Dead cells' ,'dead-cells')
    print(res)
else:
    print(res)