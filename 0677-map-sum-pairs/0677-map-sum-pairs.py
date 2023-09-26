class TrieNode:
    def __init__(self):
        self.is_end = False
        self.val = 0
        self.children = [None for _ in range(26)]


class MapSum:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, key: str, val: int) -> None:
        node = self.root
        for i in range(len(key)):
            idx = ord(key[i]) - 97
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True
        node.val = val

    def sum(self, prefix: str) -> int:
        node = self.root
        for i in range(len(prefix)):
            idx = ord(prefix[i]) - 97
            if not node.children[idx]:
                return 0
            node = node.children[idx]
        
        return node.val + self.sum_cal(node, [0])
        
            
    def sum_cal(self, node, val):
        
        for child in node.children:
            if child:
                val[0] += child.val
                self.sum_cal(child, val)
        return val[0]
                

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)