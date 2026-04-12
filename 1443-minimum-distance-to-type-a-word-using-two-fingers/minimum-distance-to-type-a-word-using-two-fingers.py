class Solution:
    def minimumDistance(self, word: str) -> int:
        w = [ord(c)-ord("A") for c in word]
        n = len(w)
        def dist(a,b):
            if a == 26:
                return 0
            r1,c1=divmod(a,6)
            r2,c2=divmod(b,6)
            return abs(r1-r2)+abs(c1-c2)
        # @cache
        # def dfs(i,other):
        #     if i == n):
        #         return 0
        #     curr = w[i]
        #     prev = w[i-1]
        #     move_curr = dist(prev,curr) + dfs(i+1,other)
        #     move_other= dist(other,curr) + dfs(i+1,prev)
        #     return min(move_curr,move_other)
        # return dfs(1,26)
        
        # TABULAR
        # dp = [[0]*27 for i in range(n+1)]
        # for i in range(n-1,0,-1):
        #     curr = w[i]
        #     prev = w[i-1]
        #     print(curr,prev)
        #     for other in range(27):
        #         move_curr = dist(prev,curr) + dp[i+1][other]
        #         move_other= dist(other,curr) + dp[i+1][prev]
        #         dp[i][other] = min(move_curr,move_other)
        # print(dp)
        # return dp[1][26]

        # space-optimized rolling two rows
        # dp[i] only ever reads from dp[i+1] — it never touches dp[i+2] or earlier
        nxt = [0] * 27   # dp[i+1]
        cur = [0] * 27   # dp[i]
        for i in range(n - 1, 0, -1):
            prev = w[i - 1]
            curr = w[i]
            for other in range(27):
                move_a = dist(prev, curr) + nxt[other]
                move_b = dist(other, curr) + nxt[prev]
                cur[other] = min(move_a, move_b)
            nxt, cur = cur, nxt   # swap — nxt now holds the row we just filled

        return nxt[26]
