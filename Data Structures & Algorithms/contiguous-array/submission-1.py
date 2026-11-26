class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = {0: -1}
        cur = 0
        res = 0 # 1, 
        # 0: -1, -1: 0, 1: 1, 
        for i, n in enumerate(nums):
            cur += 1 if n else -1
            if cur in prefix:
                res = max(res, i - prefix[cur])
            else:
                prefix[cur] = i
            
        return res