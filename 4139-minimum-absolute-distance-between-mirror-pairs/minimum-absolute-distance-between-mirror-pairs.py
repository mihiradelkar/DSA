class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        rev_map = {}
        min_dist = float('inf')
        for i,num in enumerate(nums):
            if num in rev_map:
                min_dist = min(min_dist, i-rev_map[num])
            # s = str(num)
            # r = int(s[::-1])
            r = int(str(num)[::-1])
            rev_map[r]=i
        return min_dist if min_dist != float("inf") else -1