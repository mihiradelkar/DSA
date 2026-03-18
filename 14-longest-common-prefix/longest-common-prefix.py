class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # without trie
        if not strs:
            return ""
        for index in range(len(strs[0])):
            for s in range(1,len(strs)):
                if index == len(strs[s]) or strs[0][index]!=strs[s][index]:
                    return strs[0][0:index]
        return strs[0]
        
        # Trie Node
        # if not strs: return ""
        # root = TrieNode()
        # for s in strs:
        #     node = root
        #     for c in s:
        #         if c not in node.children:
        #             node.children[c] = TrieNode()
        #         node = node.children[c]
        #     node.isEnd = True

        # prefix = ""
        # node = root
        # while True:
        #     if len(node.children)!=1 or node.isEnd:
        #         break
        #     for ch in node.children:
        #         prefix += ch
        #         node = node.children[ch]
        
        # return prefix





        