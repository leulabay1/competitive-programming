class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            idx = ord(word[i]) - 97
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        return self.dfs(word, self.root, 0)
        
    def dfs(self, word, node, i):
        if i == len(word):
            return node.is_end
        idx = ord(word[i]) - 97
        
        if idx < 0 or idx > 25:
            for child in node.children:
                if child and self.dfs(word, child, i + 1):
                    return True
        else:
            if node.children[idx]:
                return self.dfs(word, node.children[idx], i + 1)
        
        return False
        
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
        
