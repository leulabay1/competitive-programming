class TrieNode:
    def __init__(self):
        self.children = dict()
        self.count = 0
    
    def insert(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node.count += 1
            node = node.children[ch]
        node.count += 1

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        answer = [0] * len(words)
        root = TrieNode()
        for word in words:
            root.insert(word)
        
        for i in range(len(words)):
            node = root
            total = 0
            for ch in words[i]:
                node = node.children[ch]
                total += node.count
            answer[i] = total
        
        return answer