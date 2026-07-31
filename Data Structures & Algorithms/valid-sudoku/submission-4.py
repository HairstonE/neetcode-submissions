class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_set = defaultdict(set)
        box_set = defaultdict(set) # key: (row//3, col//3)
        for r in range(len(board)):
            row_set = set()
            for c in range(len(board[r])):
                cell = board[r][c]
                if cell == ".":
                    continue
                if cell in col_set[c]:
                    return False
                else: 
                    col_set[c].add(cell)
                if cell in row_set:
                    return False
                else:
                    row_set.add(cell)
                
                if cell in box_set[(r//3, c//3)]:
                    return False
                else:
                    box_set[(r//3, c//3)].add(cell)
                
        return True
                