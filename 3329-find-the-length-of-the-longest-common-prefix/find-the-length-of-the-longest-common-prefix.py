class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root1 = TrieNode()
        for num in arr1:
            node = root1
            for d in str(num):
                node.children.setdefault(d,TrieNode())
                node =  node.children[d]
        # print(root1)

        max_count = 0
        for num in arr2:
            count = 0
            node = root1
            for d in str(num):
                if d in node.children:
                    count+=1
                    node =  node.children[d]
                else:
                    break
            max_count = max(count, max_count)
        return max_count
        