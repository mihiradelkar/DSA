MX = 1_000_001
# MX = max(nums)
factors = [[] for _ in range(MX)]
for i in range(2,MX):
    if not factors[i]:
        for j in range(i,MX,i):
            factors[j].append(i)
# print(factors)
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        # n = len(nums)
        # jumps = n
        # for j in range(n-1,-1,-1):
        #     for i in range(n):
        #         if nums[j]%nums[i]==0 and nums[i]!=1:
        #             jumps = min(jumps,n-(j-i))
        # return jumps

        # n = len(nums)
        # if n == 1:
        #     return 0
        # def is_prime(x):
        #     if x<2: return False
        #     d = 2
        #     while d*d <= x:
        #         if x % d == 0:
        #             return False
        #         d+=1
        #     return True
            
        # dist = [-1] * n
        # dist[0] = 0
        # queue = deque([0])

        # while queue:
        #     i = queue.popleft()
        #     d = dist[i]
        #     if i == n-1:
        #         return d
            
        #     for ni in (i+1,i-1):
        #         if 0<=ni<n and dist[ni] == -1:
        #             dist[ni] = d+1
        #             queue.append(ni)
        #     if is_prime(nums[i]):
        #         for j in range(n):
        #             if j!=i and nums[j]%nums[i]==0 and dist[j] == -1:
        #                 dist[j] = d+1
        #                 queue.append(j)
        
        # return dist[n-1]

        # # MX = 1_000_001
        # MX = max(nums)+1
        # factors = [[] for _ in range(MX)]
        # for i in range(2,MX):
        #     if not factors[i]:
        #         for j in range(i,MX,i):
        #             factors[j].append(i)
        # # print(factors)

        n = len(nums)
        edges = defaultdict(list)
        for i, a in enumerate(nums):
            for p in factors[a]:
                edges[p].append(i)
        # print(edges)

        dist = [-1] * n
        dist[0] = 0
        queue = deque([0])

        while queue:
            i = queue.popleft()
            d = dist[i]
            if i == n-1:
                return d
            
            for ni in (i+1,i-1):
                if 0<=ni<n and dist[ni] == -1:
                    dist[ni] = d+1
                    queue.append(ni)
            
            if len(factors[nums[i]]) == 1:
                p = nums[i]
                for j in edges[p]:
                    if dist[j] == -1:
                        dist[j] = d+1
                        queue.append(j)
                edges[p].clear()
        return dist[n-1]
