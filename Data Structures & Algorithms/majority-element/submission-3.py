class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # track 2 candidates
        # if neither then subtract once the element goes negative
        # swap it
        candidates = [None, None]
        # (4, 5), (3, 1)
        for n in nums:
            if candidates[0] is None:
                candidates[0] = [1, n]
            elif candidates[1] is None and n != candidates[0][1]:
                candidates[1] = [1, n]

            elif n == candidates[0][1]:
                candidates[0][0] += 1
            elif n == candidates[1][1]:
                candidates[1][0] += 1
            else:
                candidates[0][0] -= 1
                candidates[1][0] -= 1

            if candidates[1] is not None and candidates[1][0] > candidates[0][0]:
                candidates[0], candidates[1] = candidates[1], candidates[0]

            if candidates[1] is not None and candidates[1][0] <= 0:
                candidates[1] = None

        return candidates[0][1]
