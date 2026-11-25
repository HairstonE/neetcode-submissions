class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        def bfs(row, col):
            q = deque([(row, col)])

            while q:
                r, c = q.popleft()

                dirs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

                for dr, dc in dirs:
                    if 0 <= dr < ROWS and 0 <= dc < COLS and grid[dr][dc] == "1":
                        grid[dr][dc] = "0"
                        q.append((dr, dc))

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    res += 1
                    bfs(i, j)
        return res
