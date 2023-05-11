# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        arr = []
        heapq.heapify(arr)
        
        for link in lists:
            link_temp = deque()
            cur = link
            while cur!= None:
                link_temp.append(cur.val)
                cur = cur.next
            if link_temp:
                heapq.heappush(arr, link_temp)
        ans = ListNode()
        cur = ans
        while arr:
            nodeQue = heapq.heappop(arr)
            node = nodeQue.popleft()
            newNode = ListNode(node)
            cur.next = newNode
            cur = cur.next
            if nodeQue:
                heapq.heappush(arr, nodeQue)
        return ans.next
            