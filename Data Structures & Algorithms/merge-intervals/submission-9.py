class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # sort by start
        res = [intervals[0]]
        
        for s, e in intervals[1:]:
            ts, te = res.pop()
            if s <= te:
                res.append((ts, max(te, e)))
            else:
                res.append((ts, te))
                res.append((s, e))

        return res