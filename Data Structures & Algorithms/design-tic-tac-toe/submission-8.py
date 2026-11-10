class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti = 0

    def move(self, row: int, col: int, player: int) -> int:
        
        
        self.rows[row] += 1 if player == 1 else -1
        self.cols[col] += 1 if player == 1 else -1

        for r in self.rows:
            if abs(r) == self.n:
                return 1 if r > 0 else 2

        for c in self.cols:
            if abs(c) == self.n:
                return 1 if c > 0 else 2

        r, c = 0, 0
        while r < self.n and c < self.n:
            if (r, c) == (row, col):
                self.diag += 1 if player == 1 else -1
                break
            r += 1
            c += 1

        if abs(self.diag) == self.n:
            return 1 if self.diag > 0 else 2
 
        r, c = self.n - 1, 0
        while c < self.n and r >= 0:
            if (r, c) == (row, col):
                self.anti += 1 if player == 1 else -1
                break
            r -= 1
            c += 1
        
        if abs(self.anti) == self.n:
            return 1 if self.anti > 0 else 2

        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
