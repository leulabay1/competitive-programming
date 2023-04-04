# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        odd = head
        even = head.next
        curE = even
        curO = odd
        while curE != None and curE.next != None:
            curO.next = curE.next
            curE.next = curO.next.next
            curO = curO.next
            curE = curE.next
        curO.next = even
        return odd
            