class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # n = len(points)
        # total  = 0
        # heap = [(0,0)]
        # visited = set()
        # while heap:
        #     cost, u = heapq.heappop(heap)
        #     if u in visited:
        #         continue
        #     visited.add(u)
        #     total += cost
        #     for v in range(n):
        #         if v not in visited:
        #             c = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
        #             heapq.heappush(heap,(c,v))
        # return total

        # min_cost=[inf,inf,inf,inf], 
        # available=[F,T,T,T], 
        # u=0, 
        # total=0

        n = len(points)
        min_cost = [float("inf")]*n
        available = [True] * n
        available[0] = False
        i = 0
        total = 0
        for _ in range(n-1):
            x1,y1 = points[i]
            i = 0
            for j in range(n):
                if available[j]:
                    x2,y2 = points[j]
                    cost = abs(x1-x2) + abs(y1-y2)
                    min_cost[j] = min(min_cost[j], cost)
                    i = j if min_cost[j]<min_cost[i] else i
            available[i] = False
            total += min_cost[i]
        return total