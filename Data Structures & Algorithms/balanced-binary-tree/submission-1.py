# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr):
            if not curr:
                return [True, 0]

            l_balance, l_h = dfs(curr.left)
            r_balance, r_h = dfs(curr.right)

            balance = (l_balance and r_balance and abs(l_h - r_h) <= 1)

            return [balance, 1 + max(l_h, r_h)]

        

        return dfs(root)[0]



        
        