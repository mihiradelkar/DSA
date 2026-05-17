class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # n = len(arr)
        # jumps = defaultdict(list)
        # target = None
        # for i, num in enumerate(arr):
        #     if num == 0:
        #         target = i
        #     if i+num < n:
        #         jumps[i].append(i+num)
        #     if i-num >= 0:
        #         jumps[i].append(i-num)
        # # print(jumps)
        # if not target:
        #     return False
        # queue = deque([start])
        # visited = set()
        # while queue:
        #     node = queue.popleft()
        #     if target == node:
        #         return True
        #     for j in jumps[node]:
        #         if j not in visited:
        #             queue.append(j)
        #             visited.add(j)
        # return False

        n = len(arr)
        queue = deque([start])
        # visited = {start}
        visited = [False] * n
        while queue:
            i = queue.popleft()
            if 0 == arr[i]:
                return True
            # for j in [i+arr[i], i-arr[i]]:
            #     if 0<=j<n and j not in visited:
            #         queue.append(j)
            #         visited.add(j)
            left, right = i-arr[i], i+arr[i]
            if right < n and not visited[right]:
                queue.append(right)
                visited[right]=True
            if left >= 0 and not visited[left]:
                queue.append(left)
                visited[left]=True
        return False
        