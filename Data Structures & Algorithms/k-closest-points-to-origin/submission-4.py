class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        maxHeap = []
        for x, y in points:
            dist = x*x + y*y
            heapq.heappush_max(maxHeap,[dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)
        res = []
        while maxHeap:
            out = heapq.heappop_max(maxHeap)
            res.append([out[1], out[2]])
        return res
