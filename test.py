from tictactoe import Tictactoe
import sys

class Tree:
    def __init__(self, tictactoe=Tictactoe(), depth=1):
        global i
        self.tictactoe = tictactoe
        self.child = None
        self.depth = depth

        self.score = self.get_score()
        # print(':', self.tictactoe.state)

    def get_score(self):
        if not self.tictactoe.result == 0: # game is ended
            return self.tictactoe.get_score()
        elif not self.child == None: # child is made
            return sum(map(lambda c: c.score, self.child)) / len(self.child)
            # print(self.score)
        else: # isn't ended, child isn't made
            self.make_child()
            return self.get_score()
        
    def make_child(self):
        if not self.tictactoe.result == 0: 
            raise Exception("Tree.make_child() can't be called at this situation.")
        
        self.child = []
        for pos in self.tictactoe.available_pos():
            tictactoe = Tictactoe(self.tictactoe.notation)
            tictactoe.play(pos)
            self.child.append(Tree(tictactoe, depth=self.depth+1))

tree = None
def make_tree():
    global tree
    tree = Tree()

def play_game_auto():
    game = Tictactoe()
    n_tree = tree

    while True:
        # ai turn
        # find best play
        max_score = -9999
        max_score_i = None
        for i in range(len(n_tree.child)):
            print(n_tree.child[i].score)
            if n_tree.child[i].score > max_score:
                max_score = n_tree.child[i].score
                max_score_i = i

        # get info about best play
        n_tree = n_tree.child[max_score_i]
        n_notation = n_tree.tictactoe.notation
        game.play(player=n_notation[-1]["player"], pos=n_notation[-1]["pos"], is_notation=True)

        game_state_print(game.state)

        # is end?
        if not game.result == 0:
            print("winner :", "ai" if game.result == 1 else "user")
            break

        # user turn
        user_pos = tuple(map(int, input().split()))
        game.play(user_pos)
        for i in range(len(n_tree.child)):
            if n_tree.child[i].tictactoe.notation[-1]["pos"] == user_pos:
                n_tree = n_tree.child[i]
                break

        game_state_print(game.state)

        # is end?
        if not game.result == 0:
            print("winner :", "ai" if game.result == 1 else "user")
            break
        
def play_game_auto_ai_turn():
    pass

def game_state_print(state):
    for row in state:
        for num in row:
            print(["_", "O", "X"][num], end="\t")
        print()
    print('\n')

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

def test():
    notation = [
        {"player":1, "pos": (0, 0)},
        {"player":2, "pos": (0, 1)},
        {"player":1, "pos": (0, 2)},
        {"player":2, "pos": (1, 0)},
        {"player":1, "pos": (1, 1)},
        {"player":2, "pos": (1, 2)},
        {"player":1, "pos": (2, 2)},
    ]
    t = Tictactoe()
    t.set_notation(notation)
    print(t.result)

make_tree()
play_game_auto()
# play_game_manual()
# test()