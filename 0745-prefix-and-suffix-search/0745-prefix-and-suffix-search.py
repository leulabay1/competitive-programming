class TrieNode:
    def __init__(self):
        self.children = {}
    
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = TrieNode()
        for i, word in enumerate(words):
            self.insert(word, i)
    
    def search(self, word):
        curnode =  self.trie
        
        for char in word:
            if curnode.children.get(char):
                curnode = curnode.children[char]
            else:
                return -1
        
        return [curnode, word]
    
    def insert(self, word, index):
        curnode = self.trie
        
        for char in word:
            if curnode.children.get(char):
                curnode = curnode.children[char]
            else:
                new_node = TrieNode()
                curnode.children[char] = new_node
                curnode = new_node
                
        curnode.children["*"] = index
    
    def collectwords(self, node = None, word = "", words = []):
        curnode = node
        
        for key, childnode in curnode.children.items():
            if key == "*":
                words.append([word, curnode.children[key]])
            else:
                self.collectwords(childnode, word + key, words)
        
        return words
        

    def f(self, prefix: str, suffix: str) -> int:
        tmp = self.search(prefix)
        if tmp == -1:
            return tmp
        else:
            words = self.collectwords(tmp[0], "", [])
            words.sort(key = lambda x: x[1], reverse = True)
            for word in words:
                if (tmp[1] + word[0]).endswith(suffix):
                    return word[1]
            return -1
