# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        
        def BackTracker(node, arr, path_sum):
            if not node:
                return
            if not node.right and not node.left:
                if path_sum + node.val == targetSum:
                    arr.append(node.val)
                    ans.append(arr.copy())
                    arr.pop()
                return
            
            arr.append(node.val)
            BackTracker(node.right, arr, path_sum + node.val)
            
            BackTracker(node.left, arr, path_sum + node.val)
            arr.pop()
        
        BackTracker(root, [], 0)
        return ans