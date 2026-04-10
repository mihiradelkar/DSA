class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        good = defaultdict(list)
        for i, num in enumerate(nums):
            good[num].append(i)
        # print(good)
        res = float("inf")
        for v in good.values():
            # for i in range(2,len(v)):
                # total = abs(v[i-2] - v[i-1]) + abs(v[i-1] - v[i]) + abs(v[i] - v[i-2])
            for i in range(len(v)-2):
                total = 2 * (v[i+2]-v[i]) # = (b - a) + (c - b) + (c - a)   ← all non-negative since a ≤ b ≤ c
                res = min(res,total)
        return res if res != float("inf") else -1