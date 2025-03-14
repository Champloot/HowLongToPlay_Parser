from math import gamma

from parser import parse
import optparse

def data_base_update():
    pass

if __name__ == "__main__":
    data_base_update()

    console_option_parser = optparse.OptionParser()
    console_option_parser.add_option("-g", "--game",
                                     dest="game",
                                     help="Name of game")
    (option, arguments) = console_option_parser.parse_args()
    game_name = option.game
    print(parse(game_name))