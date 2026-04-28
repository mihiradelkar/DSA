class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # flat = []
        # for g in grid:
        #     flat.extend(g)
        # flat.sort()
        # n = len(flat)
        # median = flat[n//2]
        # ops = 0
        # for num in flat:
        #     d,m = divmod(abs(num-median),x)
        #     if m != 0:
        #         return -1
        #     ops+=d
        # return ops
        flat = sorted(v for row in grid  for v in row)
        median = flat[len(flat)//2]
        ops = 0
        for v in flat:
            d, m = divmod(abs(v-median),x)
            if m != 0:
                return -1
            ops += d
        return ops
        