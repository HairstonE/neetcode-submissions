class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i, j))
        minutes = 0
        while q:
            print(len(q))
            print(q)
            print(minutes)
            for _ in range(len(q)):
                r, c = q.popleft()

                dirs = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]

                for dr, dc in dirs:
                    if 0 <= dr < ROWS and 0 <= dc < COLS and grid[dr][dc] == 1:
                        q.append((dr, dc))
                        grid[dr][dc] = 2  # now rotten
        
            minutes += 1 if q else 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1

        return minutes
