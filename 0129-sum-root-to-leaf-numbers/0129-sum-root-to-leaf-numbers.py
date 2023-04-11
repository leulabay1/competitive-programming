# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def DFS(root, arr):
            nonlocal ans
            if not root.left and not root.right:
                ans += int("".join(arr))
                return
            if root.left:
                arr.append(str(root.left.val))
                DFS(root.left, arr)
                arr.pop()
            if root.right:
                arr.append(str(root.right.val))
                DFS(root.right, arr)
                arr.pop()
        DFS(root, [str(root.val)])
        return ans