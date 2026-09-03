class Solution:
    def bfs(self, coord, grid):

        q = deque([coord])
        while q:
            r, c = q.popleft()
            
            dirs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for dr, dc in dirs:
                if 0 <= dr < self.ROWS and 0 <= dc < self.COLS and grid[dr][dc] == "1":
                    grid[dr][dc] = "0"
                    q.append((dr, dc))



    def numIslands(self, grid: List[List[str]]) -> int:
        self.ROWS = len(grid)
        self.COLS = len(grid[self.ROWS - 1])

        res = 0
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if grid[i][j] == "1":
                    res += 1
                    grid[i][j] = "0"
                    self.bfs((i, j), grid)

        return res

