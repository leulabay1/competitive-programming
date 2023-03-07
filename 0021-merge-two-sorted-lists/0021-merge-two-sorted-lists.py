# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        self.merged = ListNode()
        self.cur = self.merged
        def merge(list1, list2):
            if list1 == None or list2 == None:
                if list1 == None and list2 == None:
                    return None
                elif list1 == None:
                    self.cur.next = list2
                    self.cur = self.cur.next
                    merge(list1, list2.next)
                elif list2 == None:
                    self.cur.next = list1
                    self.cur = self.cur.next
                    merge(list1.next, list2)
            else:
                if list1.val <= list2.val:
                    self.cur.next = list1
                    self.cur = self.cur.next
                    merge(list1.next, list2)
                else:
                    self.cur.next = list2
                    self.cur = self.cur.next
                    merge(list1, list2.next)
        merge(list1, list2)
        
        return self.merged.next