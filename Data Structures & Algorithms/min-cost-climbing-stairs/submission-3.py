class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = [cost[0], cost[1]]

        for i in range(2, len(cost)):
            mem[i%2] = min(mem[0], mem[1]) + cost[i]

        return min(mem)
        