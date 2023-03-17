# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        g_max = float("-inf")
        
        def max_path(root):
            nonlocal g_max
            if not(root):
                return float("-inf")
            
            left_sum = max_path(root.left)
            right_sum = max_path(root.right)
            
            g_max = max(g_max,max(root.val, left_sum, right_sum, right_sum + root.val, left_sum +root.val, root.val + right_sum + left_sum))
            return max(root.val, root.val + right_sum, left_sum + root.val)
        max_path(root)
        
        return g_max
            
            