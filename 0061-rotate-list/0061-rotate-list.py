# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        n = 1
        while cur.next:
            cur = cur.next
            n += 1
        lastNode = cur
        
        k = k%n
        if k == 0:
            return head
        cur = head
        r = 1
        while cur.next:
            if n - k == r:
                break
            cur = cur.next
            r += 1
        oldHead = head
        head = cur.next
        cur.next = None
        lastNode.next = oldHead
        return head