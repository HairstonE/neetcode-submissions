class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list) 
        # dict{key: list(timestamp, val)}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        search = self.time_map[key]
        res = ""
        lo, hi = 0, len(search) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if search[mid][0] <= timestamp:
                res = search[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        return res

        
