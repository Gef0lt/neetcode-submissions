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
            
        maxH = 1

        stack = [root]
        heights = [1]

        while stack:
            node = stack.pop()
            h = heights.pop()
            maxH = max(h, maxH)

            if node.left:
                stack.append(node.left)
                heights.append(h+1)
            
            if node.right:
                stack.append(node.right)
                heights.append(h+1)

        return maxH
        
        