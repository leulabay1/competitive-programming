# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        cur1 = l1
        cur2 = l2
        while cur1 != None or cur2 != None:
            if cur1 != None:
                num1 += str(cur1.val)
                cur1 = cur1.next
            if cur2 != None:
                num2 += str(cur2.val)
                cur2 = cur2.next
        
        sum_value = str(int(num1) + int(num2))
        
        ans = ListNode()
        cur = ans
        for char in sum_value:
            cur.next = ListNode(int(char))
            cur = cur.next
        return ans.next