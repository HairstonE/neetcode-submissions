class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # intervals.sort(key=lambda x: x[0])
        intervals.sort()
        res = [intervals[0]]
        for s, e in intervals[1:]:
            ts, te = res.pop()
            if s <= te: # merge
                res.append([min(s, ts), max(te, e)])
            else:
                res.append([ts, te])
                res.append([s, e])
        return res