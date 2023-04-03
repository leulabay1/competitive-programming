"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        ans = 0
        if not root:
            return ans
        def Traker(root, r):
            nonlocal ans
            if not root.children:
                ans = max(ans, r)
                return
            for child in root.children:
                Traker(child, r+1)
        Traker(root, 1)
        return ans