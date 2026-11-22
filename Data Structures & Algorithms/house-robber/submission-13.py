class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        tab = [0] * len(nums)
        tab[0] = nums[0]
        tab[1] = nums[1]
        tab[2] = tab[0] + nums[2]
        for i in range(3, len(nums)):
            back2 = i - 2
            back3 = i - 3
            tab[i] = nums[i] + max(tab[back2], tab[back3])
        
        return max(tab[-1], tab[-2])
            


