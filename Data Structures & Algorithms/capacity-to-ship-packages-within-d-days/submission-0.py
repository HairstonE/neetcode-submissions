class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        res = float("inf")
        lo, hi = max(weights), sum(weights)

        while lo <= hi:
            mid = (lo + hi) // 2

            k = 0
            shipment = 0
            i = 0
            while i < len(weights):
                w = weights[i]
                shipment += w
                if (
                    i < len(weights) - 1 and mid >= shipment + weights[i + 1]
                ):  # we can add more to this shipment on the same day and not at the end
                    i += 1
                else:  # we can't add more or we are at the end, next day
                    i += 1
                    shipment = 0
                    k += 1

            if k <= days:
                hi = mid - 1
                res = min(res, mid)
            else:
                lo = mid + 1

        return res
