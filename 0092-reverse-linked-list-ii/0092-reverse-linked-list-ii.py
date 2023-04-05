# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start = 1
        firstRev = None
        prev = None
        beforeRev = None
        cur = head
        while start <= right:
            nextNode = cur.next
            if start == left:
                firstRev = cur
                prev = cur
            if start > left:
                cur.next = prev
                prev = cur
            if start < left:
                beforeRev = cur
            cur = nextNode
            start += 1
        firstRev.next = cur
        if firstRev == head:
            return prev
        else:
            beforeRev.next = prev
            return head
            
        