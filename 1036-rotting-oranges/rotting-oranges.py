class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1

        time = 0
        while queue and fresh>0:            # IMPORTANT: fresh>0: early terminate all friuts are rotten also in queue
            for i in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in  [(0,1),(1,0),(-1,0),(0,-1)]:
                    nr,nc = dr+r, dc+c
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh-=1
                        queue.append((nr,nc))
            time+=1

        return time if fresh == 0 else -1