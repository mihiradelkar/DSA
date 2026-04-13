class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
        @cache
        def dfs(i,j):
            if i==m and j==n:
                return True
            k = i+j
            res = False
            if i<m and s1[i]==s3[k]:
                res = res or dfs(i+1,j)
            if j<n and s2[j]==s3[k]:
                res = res or dfs(i,j+1)
            return res
        return dfs(0,0)
