class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        time = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j,0))

        while queue:
            rotten = len(queue)
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            for i in range(rotten):
                r,c,t= queue.popleft()
                time = max(time,t)
                for dr,dc in directions:
                    nr,nc = dr+r, dc+c
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        queue.append((nr,nc,t+1))

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return time