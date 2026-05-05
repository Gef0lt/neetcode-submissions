class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []

        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        for perm in perms:
            for i in range(len(perm) + 1):
                p_cop = perm.copy()
                p_cop.insert(i, nums[0])
                ret.append(p_cop)

        return ret
