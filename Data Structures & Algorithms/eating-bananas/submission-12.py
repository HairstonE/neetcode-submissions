class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        hi, lo = max(piles), 1
        res = float("inf")
        while lo <= hi:
            mid = (lo + hi) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / mid)
            if time <= h:
                res = min(res, mid)
                hi = mid - 1

            else:
                lo = mid + 1

        return res
