# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.vals = []

        def dfs(curr):
            if not curr:
                return
            self.vals.append(curr.val)
            dfs(curr.left)
            dfs(curr.right)

        dfs(root)

        return sorted(self.vals)[k-1]