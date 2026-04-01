class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def bfs(row,col):
            area = 0
            grid[row][col]=0
            queue = deque([(row,col)])
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            while queue:
                r, c = queue.popleft()
                area+=1
                for dr, dc in directions:
                    nr = r+dr
                    nc = c+dc
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                        grid[nr][nc]=0
                        queue.append((nr,nc))
            return area
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    max_area = max(max_area,bfs(i,j))
        return max_area
        