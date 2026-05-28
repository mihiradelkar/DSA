class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = -1

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        def is_better(a,b):
            if b == -1:
                return True
            la, lb = len(wordsContainer[a]), len(wordsContainer[b])
            if la != lb:
                return la < lb
            return a < b

        root = TrieNode()       
        for i, word in enumerate(wordsContainer):
            node = root
            if is_better(i, node.best_idx):
                node.best_idx = i
            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                if is_better(i, node.best_idx):
                    node.best_idx = i       
        result = []
        for query in wordsQuery:
            node = root
            for ch in reversed(query):
                if ch not in node.children:
                    break
                node = node.children[ch]
            result.append(node.best_idx)        
        return result