# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def find_depth(root):
            h=0
            node=root
            while node:
                h+=1
                node=node.left
            return h
        
        def bottom(root,n): # check the bottom layer node is None or Node
            path=bin(n)[2:]
            path='0'*(self.h-1-len(path))+path # fill "0" to the path 
            node=root
            for p in path:
                if p=='0':
                    node=node.left
                else:
                    node=node.right
            return node
            
        self.h=find_depth(root)
        
        i,j=0,2**(self.h-1)-1  # from 0 to 2^(h-1)-1 th botton node
        while i<=j:
            mid=(i+j)//2
            if not bottom(root,mid): # condition to find
                j=mid-1
            else:
                i=mid+1
                
        cnt=1
        for k in range(1,self.h-1):
            cnt+=2**k
        return cnt+i