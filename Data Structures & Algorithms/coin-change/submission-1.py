class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(total, ways):
            if total > amount:
                return
            if total in memo and memo[total] <= ways: 
                return
            memo[total] = min(memo[total], ways) if total in memo else ways

            for c in coins:
                dfs(total + c, ways + 1)

        dfs(0, 0)
        # print(memo)
        return memo[amount] if amount in memo else -1