class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy_price = prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - buy_price)
            buy_price = min(prices[i], buy_price)

        return res