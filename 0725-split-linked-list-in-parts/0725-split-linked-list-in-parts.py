# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size = 0
        cur = head
        while cur != None:
            size += 1
            cur = cur.next
        
        ans = []
        cur = head
        rem = size%k
        if rem:
            
            for i in range(rem):
                ans.append(cur)
                prev = cur
                for _ in range(size//k + 1):
                    prev = cur
                    cur = cur.next
                prev.next = None
                
        if cur:
            
            for i in range(rem, k):
                ans.append(cur)
                prev = cur
                for _ in range(size//k):
                    prev = cur
                    cur = cur.next
                prev.next = None
        else:
            for i in range(rem, k):
                ans.append(None)
        return ans