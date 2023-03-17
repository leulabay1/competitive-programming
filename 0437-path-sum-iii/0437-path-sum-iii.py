# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        max_sum = 0
        def sumFinder(root, pref, freq):
            nonlocal max_sum
            if not(root):
                return
            
            pref.append(pref[-1] + root.val)
            max_sum += freq.get(pref[-1] - targetSum, 0)
            freq[pref[-1]] = freq.get(pref[-1], 0) + 1
            
            
            sumFinder(root.left, pref, freq)
            sumFinder(root.right, pref, freq)
            
            freq[pref[-1]] -= 1
            
            if freq[pref[-1]] == 0:
                freq.pop(pref[-1])
            pref.pop()
            
            return
        sumFinder(root, [0], {0:1})
        return max_sum