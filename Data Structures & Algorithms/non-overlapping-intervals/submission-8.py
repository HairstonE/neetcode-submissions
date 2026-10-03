class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        prev = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prev:
                res += 1
                prev = min(prev, end)
            else:
                prev = end
                
                

        return res
