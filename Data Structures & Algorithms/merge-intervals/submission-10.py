class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        res = [intervals[0]]
        for s2, e2 in intervals[1:]:
            s1, e1 = res.pop()
            
            if s2 <= e1:
                res.append([min(s1,s2), max(e1, e2)])
            else:
                res.append([s1, e1])
                res.append([s2, e2])
        return res

