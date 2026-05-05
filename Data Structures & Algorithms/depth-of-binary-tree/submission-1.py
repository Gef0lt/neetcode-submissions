# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], i: int = 1) -> int:
        if not root:
            return 0

        l = self.maxDepth(root.left, i)
        r = self.maxDepth(root.right, i)

        return max(l, r) + 1
            

        
        