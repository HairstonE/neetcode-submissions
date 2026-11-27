class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = {0 : 1}
        res = 0
        cur = 0
        for r in range(len(nums)):
            cur += nums[r]
            res += prefix.get(cur % k, 0)
            prefix[cur % k] = prefix.get(cur % k, 0) + 1

        
        return res