class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            idx = ord(word[i]) - 97
            if node.children[idx]:
                node = node.children[idx]
            else:
                node.children[idx] = TrieNode()
                node = node.children[idx]
            if i == len(word) - 1:
                node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            idx = ord(word[i]) - 97
            if not node.children[idx]:
                return False
            if i == len(word) - 1 and not node.children[idx].is_end:
                return False
            node = node.children[idx]
        else:
            return True
            
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            idx = ord(prefix[i]) - 97
            if not node.children[idx]:
                return False
            node = node.children[idx]
        else:
            return True
        
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)