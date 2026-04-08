class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def dfs(i,rem):
            if i==n:
                return 1 if rem == 0 else 0
            if (i,rem) in memo:
                return memo[(i,rem)]
            memo[(i,rem)] = dfs(i+1,rem+nums[i]) + dfs(i+1,rem-nums[i])
            return memo[(i,rem)]
        return dfs(0,target)
            


        