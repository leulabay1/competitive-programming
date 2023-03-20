# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        temp = defaultdict(list)
        left_most = 0
        right_most = 0
        def traversing(root, row, col):
            nonlocal left_most
            nonlocal right_most
            
            if not root:
                return
            
            left_most = min(left_most, col)
            right_most = max(right_most, col)
            temp[(row, col)].append(root.val)
            
            traversing(root.left, row+1, col-1)
            traversing(root.right, row+1, col+1)
        
        traversing(root, 0, 0)
        
        ans = [[] for _ in range(right_most - left_most + 1)]
        temp = dict(sorted(temp.items(), key = lambda item: item[0][0]))
        
        for key in temp:
            ans[key[-1] - left_most] += sorted(temp[key])
        return ans