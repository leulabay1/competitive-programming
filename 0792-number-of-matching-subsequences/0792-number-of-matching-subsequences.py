class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.endOfWord = 0
        
class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.insert(word)
        
    def insert(self, word):
        cur = self.root
        for char in word:
            cur = cur.children[char]
        cur.endOfWord += 1
        
    @cache
    def countSubs(self, s, node = None, i = 0):
        if not node:
            node = self.root
            
        wordCount = node.endOfWord
        for char, child in node.children.items():
            for j in range(i, len(s)):
                if char == s[j]:
                    wordCount += self.countSubs(s, child, j + 1)
                    break
                
        return wordCount 

class Solution:
    
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie(words)
        
        return trie.countSubs(s)
        
        
        