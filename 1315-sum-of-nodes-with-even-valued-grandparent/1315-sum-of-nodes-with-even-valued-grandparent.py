# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        def DFS(root, path):
            nonlocal ans
            if not root:
                return
            if len(path) >= 3 and path[len(path)-3] % 2 == 0:
                ans += root.val
            if root.left:
                path.append(root.left.val)
                DFS(root.left, path)
                path.pop()
            if root.right:
                path.append(root.right.val)
                DFS(root.right, path)
                path.pop()
        DFS(root, [root.val])
        return ans
            