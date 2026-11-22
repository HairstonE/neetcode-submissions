class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        tab = [0] * 3
        tab[0] = nums[0]
        tab[1] = nums[1]
        tab[2] = tab[0] + nums[2]
        print(tab)
        for i in range(3, len(nums)):
            back2 = i - 2
            back3 = i - 3
            print(tab[back2%3], tab[back3%3])
            tab[i%3] = nums[i] + max(tab[back2%3], tab[back3%3])
            print(tab)
        return max(tab)
            


