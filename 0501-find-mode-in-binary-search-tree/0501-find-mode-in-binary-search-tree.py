# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        tree = {}
        def buildTree(root):
            if root == None:
                return 0
            else:
                if root.left != None:
                    buildTree(root.left)
                tree[root.val] = tree.get(root.val, 0) + 1
                if root.right != None:
                    buildTree(root.right)
            return 0
        
        buildTree(root)
        
        if len(tree) == 1:
            return [root.val]
        else:
            i = 0
            for value in tree:
                if i < tree[value]:
                    i = tree[value]
                    
            modes = []
            counter = 0
            for value in tree:
                if tree[value] == i:
                    modes.append(value)
            return modes