# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = []
        cur = head
        while cur != None:
            res.append(cur.val)
            cur = cur.next
        
        s = 0
        for i in range(len(res)//2):
            if res[i] + res[len(res)-1-i] > s:
                s = res[i] + res[len(res)-1-i]
        return s