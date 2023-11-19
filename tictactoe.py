class Tictactoe:
    def __init__(self) -> None:
        self.turn = 1
        self.state = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.notation = []
        self.result = 0 # winner
        self.auto_check = True # automatically check() after play()

    def play(self, pos: tuple, player=None) -> None:
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
        if not self.state[pos[0]][pos[1]] == 0:
            raise Exception("That position is already occupied")
        
        # change game data
        self.state[pos[0]][pos[1]] = player
        self.turn = 1 if player == 2 else 2

        # check game result
        if self.auto_check:
            self.check()

    def check(self):
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
        
        return self.result
        