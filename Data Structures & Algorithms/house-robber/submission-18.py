class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        fib = [nums[0], nums[1], nums[2] + nums[0]]

        for i, n in enumerate(nums[3:]):
            fib[i % 3] = max(fib[(i - 2) % 3], fib[((i - 3) % 3)]) + n
        return max(fib[(len(nums) - 1) % 3], fib[(len(nums) - 2) % 3])

        # 1, 2, 4
        # 3, 2, 4
        # n = 4 max([0], [2])
