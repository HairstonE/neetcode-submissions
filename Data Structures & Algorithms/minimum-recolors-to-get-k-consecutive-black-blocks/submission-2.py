class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = float('inf')
        count = 0

        i, j = 0, 0
        while j < len(blocks) and i < len(blocks):
            
            while (j - i) < (k) and j < len(blocks):
                if blocks[j] == "W":
                    count += 1
                j += 1
            print(blocks[i: j - i + 1])
            
        
            print(count)
            res = min(res, count)
            if blocks[i] == "W":
                count -= 1
            i += 1
        
        return res
