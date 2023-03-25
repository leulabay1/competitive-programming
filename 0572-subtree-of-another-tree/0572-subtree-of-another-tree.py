# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def cheaker(p, q):
            if not q and not p:
                return True
            if not q or not p:
                return False
            if q.val != p.val:
                return False
            return cheaker(p.left, q.left) and cheaker(p.right, q.right)
        def traverser(root):
            if not root:
                return False
            if root.val == subRoot.val:
                if cheaker(root, subRoot):
                    return True
            return traverser(root.left) or traverser(root.right)
        return traverser(root)
            