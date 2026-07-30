class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = dict()
        res = []
        for i, num in enumerate(nums):
            if num in comps.keys():
                return [comps[num], i]
            else:
                comps[target - num] = i

        return res