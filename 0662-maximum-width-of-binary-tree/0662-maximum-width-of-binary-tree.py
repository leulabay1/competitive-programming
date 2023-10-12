# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = dict()
        
        def dfs(node, depth, column):
            if not node:
                return
            if depth not in ans:
                ans[depth] = [-1*float("inf"), float("inf")]
            
            ans[depth][0] = max(column, ans[depth][0])
            ans[depth][1] = min(column, ans[depth][1])
            
            dfs(node.right, depth + 1, column * 2 + 1)
            
            dfs(node.left, depth + 1, column * 2)
        
        dfs(root, 0, 0)
        
        return max([ans[key_][0] - ans[key_][1] + 1 for key_ in ans])
            