import optparse
import json
import os
from time import sleep

from another_parser import DefaultError, parse


def base_check():
    file_path = 'data.json'

    if not os.path.exists(file_path):
        with open(file_path, 'w') as json_file:
            json.dump({}, json_file)

    return True


def json_operation(game, code=None):
    with open('data.json', 'r') as file:
        data = json.load(file)

    if game in data:
        return data[game]
    else:
        if code is None:
            raise DefaultError("v base net infi")
        data[game] = code

        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)


def data_update():
    cnt = 1
    err_cnt = 0
    while err_cnt < 100:
        with open('data.json', 'r') as file:
            data : dict = json.load(file)
        if not (cnt in data.values()):
            try:
                name = parse(game_code=cnt, target='name')[0]
                with open('data.json', 'w') as file:
                    data[name] = cnt
                    json.dump(data, file, indent=4)
                err_cnt = 0
            except DefaultError as e:
                err_cnt += 1
                cnt += 1

        cnt += 1


if __name__ == "__main__":
    console_option_parser = optparse.OptionParser()
    console_option_parser.add_option("-g", "--game",
                                     dest="game",
                                     help="Name of game")
    console_option_parser.add_option("-u", "--update",
                                     dest="update",
                                     help="Update the base")

    (option, arguments) = console_option_parser.parse_args()

    try:
        base_check()
        if option.game: game_name: str = option.game
        elif option.update:
            data_update()
            exit()
        game_id = json_operation(game_name)
        ans_from_parser = parse(game_id)
        print(f"Main campaign:                  ~{ans_from_parser[1]}h.\n"
              f"Campaign + additional tasks:    ~{ans_from_parser[2]}h.\n"
              f"Full playthrough:               ~{ans_from_parser[3]}h.\n")
    except DefaultError as exception:
        print("Something went wrong")
