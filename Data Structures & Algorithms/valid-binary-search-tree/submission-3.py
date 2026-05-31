# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr, mi, ma):
            if not curr:
                return True

            if not (mi < curr.val < ma):
                return False



            return dfs(curr.left, mi, curr.val) and dfs(curr.right, curr.val, ma)

        return dfs(root, float('-inf'), float('inf'))
        