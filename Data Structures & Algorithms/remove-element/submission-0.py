class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 3,2,2,3
        # val = 3
        read = 0
        k = 0
        n = len(nums) # 4
        while read + k < n:
            
            if nums[read] == val:
                nums.append(nums.pop(read))
                k += 1
            else:
                read += 1
        print(nums, end=" ")
        return n - k