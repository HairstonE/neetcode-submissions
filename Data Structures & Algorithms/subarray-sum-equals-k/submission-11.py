class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        cur = 0
        res = 0
        for i, num in enumerate(nums):
            cur += num
            res += prefix[cur - k]
            prefix[cur] += 1
        
        return res
        
