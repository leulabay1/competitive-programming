# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prevNode = None
    right = None
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root == None:
            if self.prevNode != None:
                Node = TreeNode(val)
                if self.right:
                    self.prevNode.right = Node

                else:
                    self.prevNode.left = Node
            else:
                root = TreeNode(val)
                return root
            return Node
            
        elif root.val > val:
            self.prevNode = root
            
            self.right = False
            self.insertIntoBST(root.left, val)
        elif root.val < val:
            self.prevNode = root
            self.right = True
            self.insertIntoBST(root.right, val)
        return root
        