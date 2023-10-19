# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth = 0
        
        def InOrder(node):
            nonlocal kth
            if not node:
                return
            
            left_val = InOrder(node.left)
            
            kth += 1
            
            if kth == k:
                return node.val
            
            right_val = InOrder(node.right)
            
            return right_val if right_val != None else left_val
        
        return InOrder(root)