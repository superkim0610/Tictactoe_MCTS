from tictactoe import Tictactoe

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