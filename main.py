from parser import parse, DefaultError
import optparse


if __name__ == "__main__":

    console_option_parser = optparse.OptionParser()
    console_option_parser.add_option("-g", "--game",
                                     dest="game",
                                     help="Name of game")
    (option, arguments) = console_option_parser.parse_args()
    default_game_name : str = option.game

    correct_game_name = default_game_name.lower()

    for i in range(len(correct_game_name)):
        if correct_game_name[i].isdigit():
            correct_game_name = correct_game_name[:i] + 'i'*int(correct_game_name[i]) + correct_game_name[i+1:]
            # print(correct_game_name)

    try:
        ans_from_parser = parse(correct_game_name)
        print(f"Main campaign:                  {ans_from_parser[0][0]}h. {ans_from_parser[0][1]}m.\n"
              f"Campaign + additional tasks:    {ans_from_parser[1][0]}h. {ans_from_parser[1][1]}m.\n"
              f"Full playthrough:               {ans_from_parser[2][0]}h. {ans_from_parser[2][1]}m.\n")
    except DefaultError as exception:
        print("Something went wrong")