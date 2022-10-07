# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result1 = []
        cur = l1
        while cur != None:
            result1.append(cur.val)
            cur = cur.next
        
        result2 = []
        cur = l2
        while cur != None:
            result2.append(cur.val)
            cur = cur.next
        
        s1 = ""
        for i in result1:
            s1 += str(i)
            
        s2 = ""
        for i in result2:
            s2 += str(i)
        
        sum1 = int(s1[-1::-1]) +int(s2[-1::-1])
        
        sum1 = str(sum1)
        sum1 = sum1[-1::-1]
        
        prev = ListNode(int(sum1[0]))
        ans = ListNode(0,prev)
        for i in sum1[1:]:
            newNode = ListNode(int(i))
            prev.next = newNode
            prev = newNode
        
        return ans.next
            