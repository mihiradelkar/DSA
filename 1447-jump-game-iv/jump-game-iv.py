class Solution:
    def minJumps(self, arr: List[int]) -> int:
#         # [7,6,9,6,9,6,9,7]
#         # [7,6,9,6,7,6,9,6]
#         # 
#         n = len(arr)
#         jumps = defaultdict(list)
#         # for i in range(n):
#         #     for j in range(n):
#         #         if i!=j and arr[i]==arr[j]:
#         #             jumps[i].append(j)
#         portals = defaultdict(list)
#         for i, num in enumerate(arr):
#             portals[num].append(i)

#         for i, num in enumerate(arr):
#             # jumps[num].append(i)
#             for j in portals[num]:
#                  if i!=j:
#                     jumps[i].append(j)
#             if i + 1 < n:
#                 jumps[i].append(i+1)
#             if i - 1 >= 0:
#                 jumps[i].append(i-1)
#         # print(jumps)
#         queue = deque([0])
#         visited = {0}
#         steps = 0
#         while queue:
#             for _ in range(len(queue)):
#                 curr = queue.popleft()
#                 if curr == n-1:
#                     return steps
#                 # print(curr)
#                 for nei in jumps[curr]:
#                     if nei not in visited:
#                         queue.append(nei)
#                         visited.add(nei)
#             steps+=1
#             # print(steps,queue)
#         return steps

        n  = len(arr)
        if n == 1:
            return 0
        portals = defaultdict(list)
        for i, num  in enumerate(arr):
            portals[num].append(i)
        
        queue = deque([(0,0)])
        visited = {0}
        while queue:
            curr, steps = queue.popleft()
            # print("curr",curr)
            for nei in (curr+1,curr-1):
                # print(nei)
                if 0 <= nei < n and nei not in visited:
                    if nei == n-1:
                        return steps+1
                    queue.append((nei,steps+1))
                    visited.add(nei)
            if arr[curr] in portals:
                for nei in portals[arr[curr]]:
                    # print(nei)
                    if nei not in visited:
                        if nei == n-1:
                            return steps+1
                        queue.append((nei,steps+1))
                        visited.add(nei)
                del portals[arr[curr]]
        