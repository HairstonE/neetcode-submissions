class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t = math.floor(len(nums) // 3)

        triple = [None, None, None]

        for n in nums:
            if not triple[0]:
                triple[0] = [1, n]
            elif not triple[1] and n != triple[0][1]:
                triple[1] = [1, n]
            elif not triple[2] and n != triple[0][1] and n != triple[1][1]:
                triple[2] = [1, n]
            elif triple[0][1] == n:
                triple[0][0] += 1
            elif triple[1][1] == n:
                triple[1][0] += 1
            elif triple[2][1] == n:
                triple[2][0] += 1

        print(triple)

        return [trip[1] for trip in triple if trip and trip[0] > t]
