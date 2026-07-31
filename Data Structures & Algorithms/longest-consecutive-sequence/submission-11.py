
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for num in num_set:
            if (num - 1) not in num_set:
                i = 0
                while num + i in num_set:
                    i += 1
                    res = max(res, i)
                
        return res


