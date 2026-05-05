class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_s = sorted(nums)
        i, j = 0, len(nums) - 1

        while nums_s[i] + nums_s[j] != target:
            if nums_s[i] + nums_s[j] > target:
                j -= 1
            else:
                i += 1
        
        a = nums.index(nums_s[i])
        b = len(nums) - 1 - nums[::-1].index(nums_s[j])
        return [min(a, b), max(a, b)]