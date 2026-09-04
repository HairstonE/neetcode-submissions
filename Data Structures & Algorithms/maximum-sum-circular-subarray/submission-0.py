class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        res = nums[0]
        for i, num in enumerate(nums + nums):
            cur_sum = 0
            for j in range(i, len(nums) + i):
                cur_sum += nums[j % len(nums)]
                res = max(res, cur_sum) 
        return res
