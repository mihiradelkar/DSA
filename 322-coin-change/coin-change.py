class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for a in range(1,amount+1):
            for coin in coins:
                if coin <=a:
                    dp[a] = min(dp[a],dp[a-coin]+1)
                # print(dp)
        return dp[amount] if dp[amount]!=float("inf") else -1


        # if amount == 0:
        #     return 0
        # queue = deque([amount])
        # counted = {amount}
        # steps = 0

        # while queue:
        #     steps+=1
        #     for _ in range(len(queue)):
        #         curr_rem = queue.popleft()
        #         for coin in coins:
        #             rem  = curr_rem - coin
        #             if rem == 0:
        #                 return steps
        #             if rem > 0 and rem not in counted:
        #                 queue.append(rem)
        #                 counted.add(rem)
        # return -1

        # memo = {}
        # def solve(rem):
        #     if rem < 0:
        #         return -1
        #     if rem == 0:
        #         return 0
        #     if rem in memo:
        #         return memo[rem]
        #     min_count = float('inf')

        #     for coin in coins:
        #         res = solve(rem-coin)
        #         if res != -1:
        #             min_count = min(min_count, res+1)
        #     memo[rem] = min_count if min_count != float('inf') else -1
        #     print("res: ", res, "min_count: ", min_count, memo)
        #     return memo[rem]
        # return solve(amount)
        