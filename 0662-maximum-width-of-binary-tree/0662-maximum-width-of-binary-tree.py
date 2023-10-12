# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = defaultdict(list)
        
        def dfs(node, depth, column):
            if not node:
                return
            
            ans[depth].append(column)
            
            dfs(node.right, depth + 1, column * 2 + 1)
            
            dfs(node.left, depth + 1, column * 2)
        
        dfs(root, 0, 0)
        
        return max([max(ans[key_]) - min(ans[key_]) + 1 for key_ in ans])
            