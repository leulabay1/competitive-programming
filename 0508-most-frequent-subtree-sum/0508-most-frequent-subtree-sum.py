# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        ans = {}
        def sumCounter(root):
            if not root:
                return 0

            left_sum = sumCounter(root.left)
            right_sum = sumCounter(root.right)
            subTree_sum = left_sum + right_sum + root.val
            ans[subTree_sum] = ans.get(subTree_sum,0) + 1
            return subTree_sum
        sumCounter(root)
        sorted_ans = sorted(ans.items(), key= lambda x:x[1], reverse = True)
        ans = []
        first_value = sorted_ans[0][-1]
        for i in sorted_ans:
            if i[-1] == first_value:
                ans.append(i[0])
            else:
                break
        return ans