# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
         
            ans = TreeNode(10**10)
            def dfs(node):
                nonlocal ans
                if not node:
                    return False
                self_descend = False
                if node.val == p.val or node.val == q.val:
                    self_descend = True
                right_val = dfs(node.right)
                left_val = dfs(node.left)
                
                if self_descend and (right_val or left_val):
                    ans = node
                    return False
                if right_val and left_val:
                    ans = node
                    return False
                if self_descend or right_val or left_val:
                    return True
                return False
            dfs(root)
            return ans