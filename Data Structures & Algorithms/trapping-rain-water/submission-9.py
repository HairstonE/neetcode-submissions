class Solution:
    def trap(self, height: List[int]) -> int:
        lmax, rmax = height[0], height[len(height) - 1]

        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            if lmax <= rmax:
                l += 1
                if height[l] > lmax:
                    lmax = height[l]
                else:
                    res += lmax - height[l]
            else:
                r -= 1
                if height[r] > rmax:
                    rmax = height[r]
                else:
                    res += rmax - height[r]
        return res