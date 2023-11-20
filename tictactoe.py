class Tictactoe:
    def __init__(self) -> None:
        self.turn = 1
        self.state = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.notation = []
        self.result = 0 # winner
        self.auto_check = True # automatically check() after play()

    def play(self, pos: tuple, player=None, is_notation=False) -> None:
        # player setting
        if player == None:
            player = self.turn
        else:
            # player custom setting
            pass

        # player check
        if not (player == 1 or player == 2):
            raise Exception("Player must be 1 or 2")
        
        # state check
        self.check_pos(pos)
        
        # change game data
        self.state[pos[0]][pos[1]] = player
        if not is_notation:
            self.notation.append({"player": self.turn, "pos": pos})
        self.turn = 1 if player == 2 else 2

        # check game result
        if self.auto_check:
            self.check_end()

    def check_end(self):
        # check horizontal
        for i in range(3):
            if self.state[0][i] == 0:
                continue

            if self.state[0][i] == self.state[1][i] and self.state[0][i] == self.state[2][i]:
                self.result = self.state[0][i]
                return self.result
            
        # check vertical
        for i in range(3):
            if self.state[i][0] == 0:
                continue
            
            if self.state[i][0] == self.state[i][1] and self.state[i][0] == self.state[i][2]:
                self.result = self.state[i][0]
                return self.result
            
        # check diagonal
        if not self.state[1][1] == 0:
            # right decrease
            if self.state[0][0] == self.state[1][1] and self.state[0][0] == self.state[2][2]:
                self.result = self.state[1][1]
                return self.result
            
            # right increase
            if self.state[0][2] == self.state[1][1] and self.state[0][2] == self.state[2][0]:
                self.result = self.state[1][1]
                return self.result
            
        # check draw
        if len(self.notation) == 9:
            self.result = 3
        
        return self.result

    def check_pos(self, pos):
        if not self.state[pos[0]][pos[1]] == 0:
            raise Exception("That position is already occupied")

    def set_notation(self, notation):
        self.state = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.notation = notation
        self.result = 0

        print(len(notation))
        for n_notation in notation:
            self.play(n_notation["pos"], player=n_notation["player"], is_notation=True)

    def get_score(self, player=1):
        SCORE_WIN = 30
        SCORE_LOSE = -30
        SCORE_DRAW = -10
        SCORE_EACH_TURN = -2

        score = 0
        self.check_end()
        if self.result == 3:
            score += SCORE_DRAW
        elif self.result == player:
            score += SCORE_WIN
        else:
            score += SCORE_LOSE

        score += SCORE_EACH_TURN * len(self.notation)

        return score