# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        seen = set()
        ans_seen = set()
        ans = list()
        
        def dfs(root):
            if not root:
                return ""
            
            right = dfs(root.right)
            left = dfs(root.left)
            
            subtree = str(root.val) + "right" + right + "left" + left
            if subtree in seen and subtree not in ans_seen:
                ans.append(root)
                ans_seen.add(subtree)
                
            seen.add(subtree)
            return subtree
        dfs(root)
        return ans
        