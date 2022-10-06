# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentNode = head
        result = []
        while currentNode != None:
            result.append(currentNode.val)
            currentNode = currentNode.next
            
        result = result[len(result)//2:len(result)]
        
        middle = ListNode(result[0])
        current = middle
        for i in result[1:]:
            node = ListNode(i)
            current.next = node
            current = node
        
        return middle
            
            