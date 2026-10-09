class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums: return [[lower, upper]]
        if nums[0]!= lower: nums.insert(0, lower-1)
        if nums[-1]!= upper: nums.append(upper+1)
        res = []
        
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                continue
            else:
                lb = nums[i] + 1
                ub = nums[i+ 1] - 1
                res.append([lb, ub])


        return res
