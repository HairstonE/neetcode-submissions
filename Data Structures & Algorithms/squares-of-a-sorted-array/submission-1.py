class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        res = [0]*len(nums)
        i = r
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[i] = nums[l]**2
                l += 1
            else:
                res[i] = nums[r]**2
                r -= 1
            i -= 1

        return res