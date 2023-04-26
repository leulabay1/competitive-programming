# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        que = deque()
        que.append(root)
        ans = []
        temp = deque()
        ans.append(root.val)
        while que:
            node = que.popleft()
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            
            if len(que) == 0 and len(temp):
                s = 0
                for n in temp:
                    s += n.val
                ans.append(s/len(temp))
                que = temp.copy()
                temp = deque()
        return ans                