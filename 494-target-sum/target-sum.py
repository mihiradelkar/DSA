class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def dfs(i,cur):
            if i==n:
                return 1 if cur == target else 0
            if (i,cur) in memo:
                return memo[(i,cur)]
            memo[(i,cur)] = dfs(i+1,cur+nums[i]) + dfs(i+1,cur-nums[i])
            return memo[(i,cur)]
        return dfs(0,0)
            


        