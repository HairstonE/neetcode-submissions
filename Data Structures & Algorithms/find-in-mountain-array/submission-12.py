class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # Bin search, 3 times
        # Find max, split array in 2 find elem
        # return lowest idx
        n = mountainArr.length()
        cache = [None] * n
        lo, hi = 0, n - 1
        peak = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2 
            mid_val = cache[mid] if cache[mid] else mountainArr.get(mid)
            l_val = cache[mid - 1] if cache[mid - 1] else mountainArr.get(mid - 1)
            r_val = cache[mid + 1] if cache[mid + 1] else mountainArr.get(mid + 1)
            cache[mid] = mid_val
            cache[mid - 1] = l_val
            cache[mid + 1] = r_val
            if l_val < mid_val > r_val:
                peak = mid
                break
            elif mid_val < l_val: # go left
                hi = mid - 1
            else: # go right
                lo = mid + 1

        lo, hi = 0, peak - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2 
            mid_val = cache[mid] if cache[mid] else mountainArr.get(mid)
            l_val = cache[lo] if cache[lo] else mountainArr.get(lo)
            r_val = cache[hi] if cache[hi] else mountainArr.get(hi)
            cache[mid] = mid_val
            cache[lo] = l_val
            cache[hi] = r_val
            if mid_val == target:
                return mid
            elif mid_val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        lo, hi = peak, n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2 
            mid_val = cache[mid] if cache[mid] else mountainArr.get(mid)
            l_val = cache[lo] if cache[lo] else mountainArr.get(lo)
            r_val = cache[hi] if cache[hi] else mountainArr.get(hi)
            cache[mid] = mid_val
            cache[lo] = l_val
            cache[hi] = r_val
            print(cache[lo: n])
            print(mid_val)
            if mid_val == target:
                return mid
            elif mid_val < target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return  -1