import argparse
import json
import os

from another_parser import DefaultError, parse


def base_check():
    file_path = 'data.json'

    if not os.path.exists(file_path):
        with open(file_path, 'w') as json_file:
            json.dump({}, json_file)

    return True


def json_operation(game, code=None):
    base_check()
    with open('data.json', 'r') as file:
        data = json.load(file)

    if game in data:
        return data[game]
    else:
        if code is None:
            raise DefaultError("V base net infi")
        data[game] = code

        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)


def data_update() -> str:
    base_check()
    cnt = 8000
    err_cnt = 0
    while err_cnt < 1000:
        with open('data.json', 'r') as file:
            data: dict = json.load(file)
        if not (cnt in data.values()):
            try:
                name = parse(game_code=cnt, target='name')[0]
                with open('data.json', 'w') as file:
                    data[name] = cnt
                    json.dump(data, file, indent=4)
                err_cnt = 0
            except DefaultError:
                err_cnt += 1
                cnt += 1

        cnt += 1
    return "Base was updated"


if __name__ == "__main__":
    console_option_parser = argparse.ArgumentParser()
    console_option_parser.add_argument("-g", "--game",
                                       action="store",
                                       type=str,
                                       dest="game",
                                       help="Name of game")
    console_option_parser.add_argument("-u", "--update",
                                       action="store_true",
                                       dest="update",
                                       default=False,
                                       help="Update the base")

    args = console_option_parser.parse_args()
    if args.game:
        game_name: str = args.game

        game_id = json_operation(game_name)
        ans_from_parser = parse(game_id)
        print(f"Main campaign:                  ~{ans_from_parser[1]}h.\n"
              f"Campaign + additional tasks:    ~{ans_from_parser[2]}h.\n"
              f"Full playthrough:               ~{ans_from_parser[3]}h.\n")
    elif args.update:
        print(data_update())
