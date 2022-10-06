# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
         
        dumy = ListNode(0,head)
        pre = dumy
        cur = head
        while cur != None:
            if cur.next != None and cur.val == cur.next.val:
                while cur.next != None and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return dumy.next
                