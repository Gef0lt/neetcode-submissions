class Solution:
    def maxArea(self, h: List[int]) -> int:
        l, r = 0, len(h) - 1
        max_water = 0

        while l < r:
            max_water = max(max_water, min(h[r], h[l]) * (r - l))

            if h[r] > h[l]:
                l += 1
            else:
                r -= 1

        return max_water