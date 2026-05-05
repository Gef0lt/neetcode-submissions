class Solution:
    def findMin(self, nums: List[int]) -> int:
        while len(nums) > 3:
            if nums[-1] < nums[0]:
                nums = nums[len(nums)//2 - 1:]
            elif nums[0] < nums[-1]:
                nums = nums[:len(nums)//2 + 1]

        return min(nums)

