class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        good = defaultdict(list)
        for i, num in enumerate(nums):
            good[num].append(i)
        best = float("inf")
        for v in good.values():
            if len(v)<3:
                continue
            # b-a + c-b + c-a = 2(c-a)
            for i in range(len(v)-2):
                best = min(best,(2*(v[i+2]-v[i])))
        return best if best != float("inf") else -1

        