# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symetry(q, p):
            if q == None and p == None:
                return True
            if p == None or q == None or p.val != q.val:
                return False
            else:
                left = symetry(q.left, p.right)
                right = symetry(q.right, p.left)
                return left and right
        
        return symetry(root.right, root.left)