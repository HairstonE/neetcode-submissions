class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0 

        while l < len(nums):
            if nums[l] == 0:
                for r in range(l, len(nums)):
                    if nums[r] != 0:
                        nums[l], nums[r] = nums[r], nums[l]
                        break
            l += 1