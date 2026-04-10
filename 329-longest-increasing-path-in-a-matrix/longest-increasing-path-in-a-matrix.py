class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        memo = {}
        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            best = 1
            for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr,nc = dr+r,dc+c
                if 0<=nr<m and 0<=nc<n and matrix[r][c]<matrix[nr][nc]:
                    best = max(best,1+dfs(nr,nc))
            memo[(r,c)] = best
            return best
        return max(dfs(r,c) for r in range(m) for c in range(n))