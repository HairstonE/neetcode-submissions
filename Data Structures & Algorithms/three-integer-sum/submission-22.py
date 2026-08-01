class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                value = nums[i] + nums[l] + nums[r]
                if value == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
                    while 0 <= r < len(nums) - 1 and nums[r] == nums[r+1]:
                        r -= 1
                elif value < 0:
                    l += 1
                else:
                    r -= 1
                
                
        return res
                

        