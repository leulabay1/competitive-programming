# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que = deque([root])
        temp_que = deque()
        depth = 1
        while que:
            node = que.popleft()
            if not node.left and not node.right:
                return depth
            if node.right:
                temp_que.append(node.right)
            if node.left:
                temp_que.append(node.left)
            if not que:
                que = temp_que.copy()
                temp_que = deque()
                depth += 1
        