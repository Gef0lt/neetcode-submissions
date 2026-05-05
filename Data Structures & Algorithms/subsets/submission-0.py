class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                ret.append(subset.copy())
                return

            # des to include
            subset.append(nums[i])
            dfs(i + 1)

            #def not to include nums[i]
            subset.pop()
            dfs(i + 1)
            

        dfs(0)
        return ret


