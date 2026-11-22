class Solution:
    def tribonacci(self, n: int) -> int:
        T = [0, 1, 1]
        if n < 3:
            return T[n]

        for i in range(n):
            T[i%3] = sum(T)
        
        return T[n%3]

