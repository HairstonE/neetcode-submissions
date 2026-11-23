class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if nums[mid] == target:
                return mid

            if nums[lo] <= nums[mid]: # left side sorted?
                if nums[lo] <= target < nums[mid]: # in range?
                    hi = mid - 1
                else:
                    lo = mid + 1
            else: # right side sorted?
                if nums[mid] < target <= nums[hi]: # in range?
                    lo = mid + 1
                else:
                    hi = mid - 1
            

        return -1 