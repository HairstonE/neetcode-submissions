class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    root = (i, j)
                    break

        q = deque([root])
        island = set()
        island.add(root)
        while q:
            r, c = q.popleft()
            for dr, dc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (
                    0 <= dr < ROWS
                    and 0 <= dc < COLS
                    and (dr, dc) not in island
                    and grid[dr][dc] == 1
                ):
                    q.append((dr, dc))
                    island.add((dr, dc))

        q = deque([(x, y, 0) for x, y in island])
        zero_set = set()
        while q:
            for _ in range(len(q)):
                r, c, d = q.popleft()
                for dr, dc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= dr < ROWS and 0 <= dc < COLS and (dr, dc) not in island and grid[dr][dc] == 1:
                        return d
                    if (
                        0 <= dr < ROWS
                        and 0 <= dc < COLS
                        and (dr, dc) not in zero_set
                        and grid[dr][dc] == 0
                    ):
                        q.append((dr, dc, d + 1))
                        zero_set.add((dr, dc))

        return 0
        # find 1 whole island and store as visited maybe in a q
        # multi BFS
        # Then search over 0s to find 1s not in visited set. First should be shortest.
