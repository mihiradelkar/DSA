class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Questions:
        #  can k = len(points)? return all sorted?
        #  are points int for float?
        #  single point return it
        #  negative point? x**2 will fix this

        # Approach:
        # Sort all points by distance, return first k
        # return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k] # O(nlogn) O(n)
        # 
        # Optimal: HEAP   O(n log k), O(k)
        #  dist = x**2 + y**2
        #  heappush(-dist) max dist get removed first so add -ve in front
        #  heappop() if len(heap)>k 
        #  return heap with [[x,y] for _,x,y in heap]

        heap = []
        for x, y in points:
            dist = x*x + y*y
            # dist = x**2 + y**2
            heapq.heappush(heap,(-dist,x,y))
            if len(heap)>k:
                heapq.heappop(heap)
        # res = []
        # for _ in range(k):
        #     dist,x,y = heapq.heappop(heap)
        #     res.append([x,y])
        # return res
        return [[x,y] for _,x,y in heap]