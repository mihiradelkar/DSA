class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:

        # m = len(grid)
        # n = len(grid[0])
        # dp = [[0]*n for _ in range(m)]
        # queue = deque([(0,0,0,0)])
        # while queue:
        #     r,c,cost,score = queue.popleft()
        #     print(r,c,cost,score)
        #     if cost > k:
        #         continue

        #     dp[r][c] = score
        #     for dr,dc in [(0,1),(1,0)]:
        #         nr,nc = r+dr, c+dc
        #         if nr>m or nc>n:
        #             continue
        #         if grid[nr][nc] != 0:
        #             queue.append((nr,nc,cost+1,score+grid[nr][nc]))
        #         else:
        #             queue.append((nr,nc,cost,score))
        # print(dp)
        # return -1

        # m = len(grid)
        # n = len(grid[0])
        # k = min(k, m + n - 1) 
        # @cache
        # def dp(i,j,budget):
        #     cost = 0 if grid[i][j] == 0 else 1
        #     score = grid[i][j]
        #     if budget<cost:
        #         return -1
        #     if i==0 and j==0:
        #         return score
        #     best = -1
        #     if i>0:
        #         sub = dp(i-1,j,budget-cost)
        #         if sub!=-1:
        #             best = max(best,sub+score)
        #     if j>0:
        #         sub = dp(i,j-1,budget-cost)
        #         if sub!=-1:
        #             best = max(best,sub+score)
        #     return best
        # return dp(m-1,n-1,k)
        
        # Redo
        m,n = len(grid), len(grid[0])
        INF = float("-inf")
        dp = [[[INF] * (k+1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0
        for r in range(m):
            for c in range(n):
                for cost in range(k+1):
                    if dp[r][c][cost]==INF:
                        continue
                    if r+1<m:
                        val = grid[r+1][c]
                        new_cost = 0 if val == 0  else 1
                        if cost + new_cost <= k:
                            dp[r+1][c][cost + new_cost] = max(dp[r+1][c][cost + new_cost],dp[r][c][cost]+val)
                    if c+1<n:
                        val = grid[r][c+1]
                        new_cost = 0 if val == 0  else 1
                        if cost + new_cost <= k:
                            dp[r][c+1][cost + new_cost] = max(dp[r][c+1][cost + new_cost],dp[r][c][cost]+val)
        res = max(dp[m-1][n-1])
        # print (dp)
        return -1 if res == INF else res

# [
#   [[-inf, -inf], 
#   [-inf, -inf]], 
  
#   [[-inf, -inf], 
#   [-inf, -inf]]
# ]