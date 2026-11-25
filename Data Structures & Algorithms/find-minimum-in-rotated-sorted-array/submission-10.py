class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        lo, hi = 0, len(nums) - 1
        res = float('inf')
        while lo <= hi:
            mid = (lo + hi) // 2

            res = min(nums[mid], res)

            if nums[mid] < nums[hi]: # right side sorted
                hi = mid - 1

            else: # left side sorted
                lo = mid + 1

        return res

            