# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(root1, root2, prevNode, right):
            if root1 == None and root2 == None:
                return None
            elif root1 == None and root2 != None:
                if right:
                    prevNode.right = root2
                    return None
                else:
                    prevNode.left = root2
                    return None
            elif root1 != None and root2 != None:
                root1.val = root1.val + root2.val
                merge(root1.right, root2.right,root1, True)
                merge(root1.left, root2.left,root1, False)
            return prevNode
        
        if root1 == None and root2 == None:
            return None
        elif root1 == None:
            return root2
        elif root2 == None:
            return root1
        else:
            merge(root1.left, root2.left, root1, False)
            merge(root1.right, root2.right, root1, True)
            root1.val = root1.val + root2.val
            return root1