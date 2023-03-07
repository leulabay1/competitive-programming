# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            else:
                cur = root.right
                while cur.left != None:
                    cur = cur.left
                    
                temp = cur
                self.deleteNode(root, temp.val)
                root.val = temp.val
                return root
        return root