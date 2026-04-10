class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #  l =     2               3            4              5
        #  i = [0 1 2 3]        [0 1 2]       [0 1]           [0]
        #  j = [2 3 4 5]        [3 4 5]       [4 5]           [5]
        #  k = [1][2][3][4] [1 2][2 3][3 4] [1 2 3][2 3 4] [1 2 3 4]
        #                                                         ^

        #    [ 1,  3,  1,  5,  8,  1] 159+8+0
        #   [[ 0,  0,  3, 30,159,167], 
        #    [ 0,  0,  0, 15,135,159], 
        #    [ 0,  0,  0,  0, 40, 48], 
        #    [ 0,  0,  0,  0,  0, 40], 
        #    [ 0,  0,  0,  0,  0,  0], 
        #    [ 0,  0,  0,  0,  0,  0]]
        
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for length in range(2,n):
            for i in range(n-length):
                j = i + length
                for k in range(i+1,j):
                    coins = nums[i] * nums[k] * nums[j]
                    # print(("coins:",coins), (nums[i], nums[k], nums[j]))
                    total = dp[i][k] + coins + dp[k][j]
                    # print((i,k),(k,j),("prev:",dp[i][j]),("total:",total),(dp[i][k], coins, dp[k][j]))
                    dp[i][j] = max(dp[i][j],total)
        # print(dp)
        return dp[0][n-1]