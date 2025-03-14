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
    ans = parse(game_name)
    print(f"Main campaign:                  {ans[0][0]}h. {ans[0][1]}m.\n"
          f"Campaign + additional tasks:    {ans[1][0]}h. {ans[1][1]}m.\n"
          f"Full playthrough:               {ans[2][0]}h. {ans[2][1]}m.\n")