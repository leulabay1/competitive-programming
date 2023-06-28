# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(float('inf'))
        dummy.next = head
        pre1 = head
        ptr1 = head.next
        while ptr1: # keep the loop invariant that nodes between dummy and ptr1 are sorted
            pre2 = dummy
            ptr2 = dummy.next
            while ptr2 != ptr1 and ptr2.val <= ptr1.val: # ptr2 searches for the right place to insert ptr1
                pre2 = ptr2
                ptr2 = ptr2.next
            if ptr2 == ptr1:
                pre1 = ptr1
                ptr1 = ptr1.next
            else:
                pre2.next = ptr1
                tmp = ptr1.next
                ptr1.next = ptr2
                ptr2 = ptr1
                ptr1 = tmp
                pre1.next = ptr1
        return dummy.next