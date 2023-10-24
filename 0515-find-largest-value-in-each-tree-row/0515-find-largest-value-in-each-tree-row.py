# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        
        def dfs(node, depth):
            if not node:
                return
            
            if len(ans) < depth:
                ans.append(node.val)
            else:
                ans[depth - 1] = max(ans[depth - 1], node.val)
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 1)
        
        return ans