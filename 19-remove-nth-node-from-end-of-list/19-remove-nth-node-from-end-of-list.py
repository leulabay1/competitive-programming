# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        size = 0
        cur = head
        while cur != None:
            cur = cur.next
            size += 1
        if size == 1:
            return None
        
        dumy = ListNode(0,head)
        cur = dumy
        for i in range(size - n):
            cur = cur.next
        cur.next =cur.next.next
        
        return dumy.next