class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        nums = [(v, k) for k, v in counts.items()]
        heapq.heapify_max(nums)
        res = []
        
        while nums and k > 0:
            res.append(heapq.heappop_max(nums)[1])
            k -= 1
        return res