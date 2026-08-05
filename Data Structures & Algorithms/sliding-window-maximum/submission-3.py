class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        # use a heap of (num, idx)
        # grow heap until size k
        # append current max
        # only shrink heap if idx is < left pointer
        # pop max into res
        heap = []
        for r in range(len(nums)):
            heapq.heappush_max(heap, (nums[r], r))
            # Once the window is at least size k
            if r >= k - 1:
                left = r - k + 1
                while heap[0][1] < left:
                    heapq.heappop_max(heap)

                res.append(heap[0][0])
        return res

