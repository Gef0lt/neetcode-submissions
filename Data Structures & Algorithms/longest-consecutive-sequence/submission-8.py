class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        s = set(nums)

        ans = 0
        l = 0

        for el in s:
            if el-1 not in s:
                l = 1
                while el + l in s:
                    l += 1
                ans = max(ans, l)
        
        return ans