class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # s1 = "aabcc", s2 = "dbbca", 
        # s3 = "aadbbcbcac"

        # s1 s2->""    d     b      b      c       a
        # "" [[True, False, False, False, False, False], 
        # a  [True, False, False, False, False, False], 
        # a  [True, False, False, False, False, False], 
        # b  [False, False, False, False, False, False], 
        # c  [False, False, False, False, False, False], 
        # c  [False, False, False, False, False, False]]
        # i= 1
        # j= 1
        # k= 1

        # REDO 

        # m = len(s1)
        # n = len(s2)
        # if m + n != len(s3):
        #     return False
        # dp = [[False]*(n+1) for _ in range(m+1)]
        # dp[0][0] = True
        # for i in range(1,m+1):
        #     dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        # for j in range(1,n+1):
        #     dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        
        # for i in range(1,m+1):
        #     for j in range(1,n+1):
        #         k = i+j-1
        #         # print(dp[i-1][j],i,":", s1[i-1],k,":", s3[k])
        #         from_s1 = (dp[i-1][j] and s1[i-1] == s3[k])
        #         # print(dp[i][j-1],i,":", s1[j-1],k,":", s3[k])
        #         from_s2 = (dp[i][j-1] and s2[j-1] == s3[k])
        #         dp[i][j] = from_s1 or from_s2
        #         # dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[k]) or (dp[i][j-1] and s2[j-1] == s3[k])
        # # print(dp)
        # return dp[m][n]
        
        # decision tree
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
        memo = {}
        def dfs(i,j):
            if i==m and j==n:
                return True
            if (i,j) in memo:
                return memo[(i,j)]
            k = i+j
            res = False
            if i<m and s1[i]==s3[k]:
                res = res or dfs(i+1,j)
            if j<n and s2[j]==s3[k]:
                res = res or dfs(i,j+1)
            memo[(i,j)] = res
            return res
        return dfs(0,0)

