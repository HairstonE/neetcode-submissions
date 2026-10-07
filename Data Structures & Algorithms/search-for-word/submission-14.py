class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        # "a","b"
        # "c","d"
        def dfs(i, j, index, visit):
            
            if index == len(word):
                return True
            if (i, j) in visit:
                return False
            
            if not (0 <= i < ROWS) or not (0 <= j < COLS):
                return False
            if board[i][j] == word[index]:
                visit.add((i, j))
                index += 1
                if (
                    dfs(i + 1, j, index, visit)
                    or dfs(i - 1, j, index, visit)
                    or dfs(i, j + 1, index, visit)
                    or dfs(i, j - 1, index, visit)
                ): return True
                visit.remove((i, j))
            return False

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0, set()):
                    return True
        return False
