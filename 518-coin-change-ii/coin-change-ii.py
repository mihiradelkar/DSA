class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [0] * (amount+1)
        ways[0] = 1
        for coin in coins:
            for a in range(coin,amount+1):
                ways[a] = ways[a] + ways[a-coin]
        return ways[amount]







        # amount = 5
        # coins  = [1,2,5]
        # dp   = [1,1,1,1,1,1]
        
        # ways[2] = ways[2] + ways[1]
        # ways[2] =    1    +   1    = 2
        # ways[3] = ways[3] + ways[1]
        # ways[3] =    1    +   1    = 2

        # dp = [0] * (amount + 1)   # dp[a] = ways to make amount a
        # dp[0] = 1                  # base case: 1 way to make 0 (use nothing)
        # # print(dp)
        # for coin in coins:         # outer loop = coins → guarantees combinations
        #     for a in range(coin, amount + 1):  # only update amounts >= coin
        #         print("coin: ",coin," amount: ",amount," a: ",a)
        #         dp[a] += dp[a - coin]  # use this coin: add ways to make (a - coin)
        #         print(dp)

        # return dp[amount]          # answer: ways to make target amount

        # res = 0
        # short = {}
        # for i in range(len(coins)-1,-1,-1):
        #     remainder = amount%coins[i]
        #     print(coins[i])
        #     if remainder==0:
        #         res+=1
        #     else:
        #         short[remainder]=short.get(remainder, 0) + 1 
        #         print(short)
        #     if coins[i] in short:
        #         res += short[coins[i]]
        # return res