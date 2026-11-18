class TimeMap:

    def __init__(self):
        self.kv = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        res = -1
        lo, hi = 0, len(self.kv[key]) - 1

        while lo <= hi:
           
            mid = (lo + hi) // 2

            if self.kv[key][mid][0] <= timestamp:
                
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return self.kv[key][res][1] if res != -1 else ""