# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def find_max(node):
            if not node : return 0 
            left = 1 + find_max(node.left)
            right = 1 + find_max(node.right)

            return max(left,right)
        
        depth = find_max(root)
        ans = [[] for _ in range(depth)]
        
        def levelTraversing(p, level):
            if p == None:
                return 0
            else:
                ans[level].append(p.val)
                if p.left != None:
                    levelTraversing(p.left, level + 1)
                if p.right != None:
                    levelTraversing(p.right, level + 1)
            
            return 0
        levelTraversing(root, 0) 
        
        return ans