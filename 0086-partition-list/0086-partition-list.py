# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessNode = ListNode()
        higherNode = ListNode()
        curLess = lessNode
        curHigh = higherNode
        cur = head
        
        while cur != None:
            if cur.val < x:
                curLess.next = cur
                curLess = curLess.next
            else:
                curHigh.next = cur
                curHigh = curHigh.next
            cur = cur.next
        curHigh.next = None
        curLess.next = higherNode.next
        return lessNode.next