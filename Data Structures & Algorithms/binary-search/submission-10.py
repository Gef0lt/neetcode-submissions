class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        while len(nums) > 1:
            if len(nums) % 2 == 0:
                if nums[len(nums) // 2] <= target:
                    start += len(nums) // 2
                    nums = nums[len(nums) // 2:]
                else:
                    nums = nums[:len(nums) // 2]
            else:
                if nums[len(nums) // 2] == target:
                    return start + (len(nums) // 2)
                elif nums[len(nums) // 2] < target:
                    start += len(nums) // 2 + 1
                    nums = nums[len(nums) // 2 + 1:]
                else:
                    nums = nums[:len(nums) // 2]
        if nums[0] == target:
            return start
        return -1