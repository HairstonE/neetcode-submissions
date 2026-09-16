class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[ROWS - 1])
        
        res = []
        pacific_set = set()
        atlantic_set = set()
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or j == 0:
                    pacific_set.add((i, j))
                if i == ROWS - 1 or j == COLS - 1: 
                    atlantic_set.add((i, j))

    
        def bfs(xy_set) -> set:
            q = deque([t for t in xy_set])
            while q:
                r, c = q.popleft()
                dirs = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for dr, dc in dirs:
                    if 0 <= dr < ROWS and 0 <= dc < COLS and (dr, dc) not in xy_set and heights[r][c] <= heights[dr][dc]:
                        q.append((dr,dc))
                        xy_set.add((dr, dc))
            return xy_set

        pacific_set = bfs(pacific_set)
        atlantic_set = bfs(atlantic_set)
        return [[x, y] for x,y in pacific_set.intersection(atlantic_set)]
        