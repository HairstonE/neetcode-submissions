class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        hold_price = prices[0]
        for p in prices[1:]:
            res = max(res, p - hold_price)
            hold_price = min(hold_price, p)
        return res