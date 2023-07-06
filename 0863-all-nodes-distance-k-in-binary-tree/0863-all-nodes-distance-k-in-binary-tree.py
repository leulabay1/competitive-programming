# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
    def build_graph(self, node, parent):
        if not node:
            return
        if parent:
            self.graph[node.val].append(parent.val)
            self.graph[parent.val].append(node.val)
        self.build_graph(node.right, node)
        self.build_graph(node.left, node)
        return
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        self.build_graph(root, None)
        
        ans = []
        que = deque([(target.val, 0)])
        visited = set()
        while que:
            val, dist = que.popleft()
            visited.add(val)
            if dist == k:
                ans.append(val)
            for node in self.graph[val]:
                if node not in visited:
                    que.append((node, dist+1))
        return ans
            