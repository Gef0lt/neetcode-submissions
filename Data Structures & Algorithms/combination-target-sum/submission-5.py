class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        
        def f(nums, i, target, curr_comb, curr_sum):
            if curr_sum == target:
                self.res.append(curr_comb.copy())
                return
            if curr_sum > target:
                return 
            if i >= len(nums):
                return

            curr_comb.append(nums[i])
            f(nums, i, target, curr_comb, curr_sum + nums[i])
            curr_comb.pop()
            f(nums, i + 1, target, curr_comb, curr_sum)
        

        f(nums, 0, target, [], 0)

        return self.res
        

