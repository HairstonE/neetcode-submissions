class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(curr: List[int], idx: int):
            s = sum(curr)
            if  s == target and curr not in res:
                res.append(curr[:])
                return
            elif s > target: 
                return 
            
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                dfs(curr, i)
                curr.pop()

        dfs([], 0)
        return res