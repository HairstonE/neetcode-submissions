class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t = math.floor(len(nums) // 3)

        triple = [None, None]

        for n in nums:
            if not triple[0]:
                triple[0] = [1, n]
            elif not triple[1] and n != triple[0][1]:
                triple[1] = [1, n]
            elif triple[0][1] == n:
                triple[0][0] += 1
            elif triple[1][1] == n:
                triple[1][0] += 1
            else:
                triple[0][0] -= 1
                triple[1][0] -= 1
            if triple[0][0] <= 0:
                triple[0] = None
            if triple[1] and triple[1][0] <= 0:
                triple[1] = None

        counter = {}
        for n in nums:
            if triple[0] and n == triple[0][1] or triple[1] and n == triple[1][1]:
                counter[n] = counter.get(n, 0) + 1

        return [k for k, v in counter.items() if v > t]
