# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def searcher(root):
            if root == None:
                return 0, 0

            L_val, lt_val = searcher(root.left)

            R_val, rt_val  = searcher(root.right)

            root_val = root.val

            root.val = L_val - R_val

            return R_val + L_val + root_val, abs(root.val) + lt_val + rt_val
        val, ans = searcher(root)
        return ans
        
        
        