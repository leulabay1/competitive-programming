# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(prev, node, nextnode):
            if nextnode == None:
                return node
            prev.next = nextnode
            node.next = nextnode.next
            nextnode.next = node
            prev = node
            if node.next == None:
                return nextnode
            swap(prev, node.next, node.next.next)
            return nextnode
        if head == None:
            return head
        return swap(head, head, head.next)