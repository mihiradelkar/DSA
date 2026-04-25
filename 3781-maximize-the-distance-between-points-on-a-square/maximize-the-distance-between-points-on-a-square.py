class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # 0  1  2   3      4
        # 00    20  21 12  22
        dist = []
        for x,y in points:
            if x == 0:
                dist.append(y)
            elif y == side:
                dist.append(side + x)
            elif x == side:
                dist.append(3*side - y)
            else:
                dist.append(4*side - x)
        # print(dist)
        dist.sort()
        def check(limit):
            p = side * 4
            for start in dist:
                end = start + p - limit
                cur = start
                for _ in range(k-1):
                    idx = bisect_left(dist,cur + limit)
                    if idx == len(dist) or dist[idx] > end:
                        cur = -1
                        break
                    cur = dist[idx]
                if cur >= 0:
                    return True
            return False
        lo, hi = 1, side
        res = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid + 1
                res = mid
            else:
                hi = mid -1
        return res
        