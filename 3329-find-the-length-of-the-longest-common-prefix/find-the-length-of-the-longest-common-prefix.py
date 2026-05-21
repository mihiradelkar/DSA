# class TrieNode:
#     def __init__(self):
#         self.children = {}

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # WITHOUT STR CONVERSION
        prefix = set()
        for num in arr1:
            while num>0:
                prefix.add(num)
                num//=10
        # print(prefix)
        max_num = 0
        for num in arr2:
            while num>max_num:
                if num in prefix:
                    max_num = num
                    break
                num//=10
        return len(str(max_num)) if max_num else 0

        # HASH SET APPROACH
        # prefix = set()
        # for num in arr1:
        #     s = str(num)
        #     for i in range(1,len(s)+1):
        #         prefix.add(s[:i])
        # # print(prefix)
        # max_count = 0
        # for num in arr2:
        #     s = str(num)
        #     for i in range(1,len(s)+1):
        #         if s[:i] in prefix:
        #             max_count = max(i, max_count)
        #         else:
        #             break
        # return max_count

        # TRIE APPROACH
        # root1 = TrieNode()
        # for num in arr1:
        #     node = root1
        #     for d in str(num):
        #         node.children.setdefault(d,TrieNode())
        #         node =  node.children[d]
        # # print(root1)

        # max_count = 0
        # for num in arr2:
        #     count = 0
        #     node = root1
        #     for d in str(num):
        #         if d in node.children:
        #             count+=1
        #             node =  node.children[d]
        #         else:
        #             break
        #     max_count = max(count, max_count)
        # return max_count
