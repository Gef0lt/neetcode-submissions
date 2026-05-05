class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)

        return False