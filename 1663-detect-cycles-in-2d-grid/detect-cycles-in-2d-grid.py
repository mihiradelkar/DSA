class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]

        def dfs(r,c,pr,pc,ch):
            if r<0 or r>=m or c<0 or c>=n:
                return False
            if grid[r][c] != ch:
                return False
            if visited[r][c]:
                return True
            visited[r][c] = True

            for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr,nc = r+dr, c+dc
                if (nr,nc) == (pr,pc):
                    continue
                if dfs(nr,nc,r,c,ch):
                    return True
            return False
        for r in range(m):
            for c in range(n):
                if not visited[r][c]:
                    if dfs(r,c,-1,-1,grid[r][c]): 
                        return True
        return False