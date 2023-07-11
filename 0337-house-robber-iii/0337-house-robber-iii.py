# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root:
            return [0, 0]
        leftPair = self.helper(root.left)
        rightPair = self.helper(root.right)
        
        withRoot = root.val + leftPair[1] + rightPair[1]
        withOutRoot = max(leftPair) + max(rightPair)
        return [withRoot, withOutRoot]
        
    def rob(self, root: Optional[TreeNode]) -> int:
        
        return max(self.helper(root))