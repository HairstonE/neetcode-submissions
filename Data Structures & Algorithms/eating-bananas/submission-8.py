class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        res = max(piles)
        while lo <= hi:
            eating_speed = (lo + hi) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/eating_speed)
            if hours <= h:
                res = eating_speed
                hi = eating_speed - 1
            else:
                lo = eating_speed + 1
        
        return res