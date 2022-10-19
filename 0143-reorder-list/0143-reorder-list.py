# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        cur = head
        while cur != None:
            arr.append(cur)
            cur = cur.next
        
        if len(arr) <= 1:
            return head
        
        i = 0
        j = len(arr)-1
        while i < len(arr)//2-1:
            arr[i].next = arr[j]
            arr[j].next = arr[i+1]
            i+=1
            j-=1
        if len(arr)%2 == 0:
            arr[i].next = arr[j]
            arr[j].next = None
        else:
            arr[i].next = arr[j]
            arr[j].next = arr[i+1]
            arr[i+1].next = None
        