class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        # T = [2,1,4,5], 
        # S = [1,2,3,4]
        # AS = [[0,1],[2,3]]
        # a = 0
        # b = 1
        # abs(ai-aj)
        # abs(bi-bj)

        n = len(source)
        parent = {}
        def find(x):
            if parent.setdefault(x,x) != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            parent[find(y)] = find(x)

        for x,y in allowedSwaps:
            union(x,y)

        group = defaultdict(Counter)
        for i in range(n):
            group[find(i)][source[i]]+=1
        # print(parent)
        # print(group)
        dist = 0
        for i in range(n):
            root = find(i)
            if group[root][target[i]]>0:
                group[root][target[i]]-=1
            else:
                dist+=1
        return dist
        
        