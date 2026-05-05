# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def getHeight(root):
    if not root:
        return 0
    return 1 + max(getHeight(root.left), getHeight(root.right))

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                if abs(getHeight(node.left) - getHeight(node.right)) > 1:
                    return False

        return True