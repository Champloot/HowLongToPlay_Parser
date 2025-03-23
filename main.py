import optparse
import json
from another_parser import DefaultError, parse


def json_operation(game_name, code=None):
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    if game_name in data:
        return data[game_name]
    else:
        if code is None:
            raise DefaultError("v base net infi")
        data[game_name] = code

        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)


if __name__ == "__main__":
    console_option_parser = optparse.OptionParser()
    console_option_parser.add_option("-g", "--game",
                                     dest="game",
                                     help="Name of game")
    (option, arguments) = console_option_parser.parse_args()
    game_name: str = option.game
    game_id = json_operation(game_name)
    try:
        ans_from_parser = parse(game_id)
        print(f"Main campaign:                  ~{ans_from_parser[0]}h.\n"
              f"Campaign + additional tasks:    ~{ans_from_parser[1]}h.\n"
              f"Full playthrough:               ~{ans_from_parser[2]}h.\n")
    except DefaultError as exception:
        print("Something went wrong")
