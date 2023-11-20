from tictactoe import Tictactoe


def play_game_manual():
    game = Tictactoe()

    while True:
        state = game.state
        for l in state:
            print(" ".join(map(str, l)))
        print('turn :', game.turn)
        game.play(tuple(map(int, input().split())))
        print('\n\n')

        if not game.result == 0:
            print("winner :", game.result)
            break

    for _ in game.notation:
        print(_)
    print(game.get_score())

class Tree:
    def __init__(self):
        pass

# play_game_manual()