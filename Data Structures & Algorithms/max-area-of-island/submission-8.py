class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    grid[i][j] = 0
                    q = [(i, j)]
                    curr_size = 0
                    while q:
                        r, c = q.pop(0)
                        curr_size += 1
                        
                        for dr, dc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                            if 0 <= dr < ROWS and 0 <= dc < COLS and grid[dr][dc]:
                                q.append((dr, dc))
                                grid[dr][dc] = 0
                                
                    res = max(res, curr_size)

        return res

