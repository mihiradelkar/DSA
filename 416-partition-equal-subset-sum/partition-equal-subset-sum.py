class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # set and add all sums and value
        # total = sum(nums)
        # if total % 2 != 0: return False
        # target = total // 2
        # myset = set([0])
        # for num in nums:
        #     newset = set()
        #     for value in myset:
        #         if target == value+num or target == num : return True
        #         newset.add(value+num)
        #         newset.add(value)
        #     myset = newset
        # return False


        # for num in nums:
        #     for i in range(target,num-1,-1):
        #         if dp[i]: continue
        #         if dp[i-num]: dp[i] = True
        #         if dp[-1]: return True
        # return False

        # with dp 0/1 knapsack
        total  = sum(nums)
        if total%2 == 1:
            return False
        target = total//2
        dp = [False] * (target+1)
        dp[0] = True
        for num in nums:
            for j in range(target,num-1,-1):
                dp[j] = dp[j] or dp[j-num]
            if dp[target]:
                return True
        return dp[target]
        