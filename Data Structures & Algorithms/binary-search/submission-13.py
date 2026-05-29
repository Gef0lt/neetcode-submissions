class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binSearch(nums, l, r):
            if l > r:
                return -1

            m = l + (r - l) // 2
            if nums[m] > target:
                return binSearch(nums, l, m - 1)
            elif nums[m] < target:
                return binSearch(nums, m + 1, r)
            else:
                return m

        return binSearch(nums, 0, len(nums) - 1)

