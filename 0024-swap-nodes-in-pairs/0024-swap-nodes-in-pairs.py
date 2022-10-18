# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        dummie = head.next
        cur = pre = head
        if cur and cur.next != None:
            nextNode = cur.next
            cur.next = cur.next.next
            nextNode.next = cur
            pre = cur
            cur = cur.next
            
        while cur and cur.next != None:
            nextNode = cur.next
            cur.next = cur.next.next
            nextNode.next = cur
            pre.next = nextNode
            pre = cur
            cur = cur.next
            
        return dummie
            
        