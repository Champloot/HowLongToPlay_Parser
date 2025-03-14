import sqlite3


def main(cmd='select', *args):
    db = sqlite3.connect('games.db')

    # Create cursor
    global curs
    curs = db.cursor()

    match cmd:
        case 'add':
            update_game_name_table(*args)
        case 'del':
            del_from_game_name_table(*args)
        case 'select':
            res = select_from_game_name_table(*args)
            print(res)
        case '__reCreate':
            create_game_name_table()
        case _:
            pass

    # update_game_name_table('Dead Cells', 'dead-cells')
    # print(select_from_game_name_table('Dead Cells'))

    db.commit()
    db.close()


def create_game_name_table():
    # Здесь создаётся таблица для корректной подстановки названия игры в поисковую строку.
    # Будет два столбца:
    #     standard_name - то, как назвал бы игру пользователь. Типа "Dead Cells" или "Dark Souls 3"
    #     correct_name - то, как он указывается в поисковике. Типа "dead-cells"

    curs.execute("""
    CREATE TABLE game_names (
        standard_name text,
        correct_name text
    )
    """)

def del_from_game_name_table(standard_name):
    curs.execute(f"DELETE FROM game_names WHERE standard_name=={standard_name}")

def update_game_name_table(standard_name, correct_name):
    curs.execute(f"INSERT INTO game_names VALUES ('{standard_name}','{correct_name}')")

def select_from_game_name_table(standard_name):
    curs.execute(f"SELECT * FROM game_names WHERE standard_name=='{standard_name}'")
    return curs.fetchone()[1]


if __name__ == "__main__":
    main('select', 'Dead Cells')
