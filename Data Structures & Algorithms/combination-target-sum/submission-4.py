class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        stack = []
        ans = []
        for i in range(len(nums)):
            stack.append([[nums[i]], nums[i], i]) # set, sum, pos

        while stack:
            curr = stack.pop()
            if curr[1] == target:
                ans.append(curr[0])
            elif curr[1] > target:
                continue
            else:
                for i in range(curr[2], len(nums)):
                    stack.append([curr[0] + [nums[i]], curr[1] + nums[i], i])

        return ans
