# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        cur = head
        while cur != None:
            res.append(cur.val)
            cur = cur.next
        
        a = 0
        b = len(res)-1
        for i in range(len(res)//2):
            if res[a] != res[b]:
                return False
            a += 1
            b -= 1
        else:
            return True
        