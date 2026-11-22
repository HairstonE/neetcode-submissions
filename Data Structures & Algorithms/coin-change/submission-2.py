class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        best = [float('inf')] * (amount + 1)
        best[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    ways = best[i - c] + 1
                    best[i] = min(ways, best[i])

        return best[amount] if best[amount] != float('inf') else -1





        