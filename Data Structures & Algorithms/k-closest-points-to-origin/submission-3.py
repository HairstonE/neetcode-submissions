class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Top k == heap
        distance_triple = [[x*x + y*y, x, y] for x, y in points]
        heapq.heapify(distance_triple)
        res = []
        for _ in range(k):
            d, x, y = heapq.heappop(distance_triple)
            res.append([x, y])
        return res

