class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        mem = [1, 2]

        for i in range(2, n):
            mem[i%2] = mem[(i-1)%2] + mem[(i-2)%2]

        
        return max(mem)
