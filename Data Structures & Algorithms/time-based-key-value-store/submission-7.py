class TimeMap:

    def __init__(self):
        self.kv = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        arr = self.kv[key]
        if not arr: return ""
        lo, hi = 0, len(arr) - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2

            if arr[mid][0] <= timestamp:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return arr[ans][1] if ans != -1 else ""
        
        
