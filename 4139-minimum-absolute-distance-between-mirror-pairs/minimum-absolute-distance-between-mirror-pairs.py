class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        rev_map = {}
        dist = float('inf')
        for i,num in enumerate(nums):
            if num in rev_map:
                dist = min(dist, i-rev_map[num])
            # s = str(num)
            # r = int(s[::-1])
            # rev_map[r]=i
            rev_map[int(str(num)[::-1])]=i
        return dist if dist != float("inf") else -1