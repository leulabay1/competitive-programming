# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sum1 = 0
        def tracker(root):
            nonlocal sum1
            if not root:
                return
            sum1 += root.val
            tracker(root.left)
            tracker(root.right)
            
        def replacer(root, backSum):
            nonlocal sum1
            if not root:
                return 0
            leftSum = replacer(root.left, backSum)
            rightSum = replacer(root.right, backSum + leftSum + root.val)
            rootval = root.val
            root.val = sum1 - leftSum - backSum
            return leftSum + rightSum + rootval
        tracker(root)
        replacer(root, 0)
        return root
        