class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # count size of an island and mark it with id
        def dfs(r,c,iid):
            if r<0 or r>=n or c<0 or c>=n:
                return 0
            if grid[r][c] != 1:
                return 0
            grid[r][c] = iid
            size = 1
            for dr, dc in ((0,1),(1,0),(0,-1),(-1,0)):
                size += dfs(r+dr,c+dc,iid)
            return size
        
        island_id = 2                   #start from 2
        island_size = {} #defaultdict(int)
        # start numbering and counting size of islands
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    island_size[island_id] = dfs(row,col,island_id)
                    island_id+=1            
        # print(grid,island_size)

        # search all 4 direction for island and add sizes and compare it with max
        res = max(island_size.values(),default=0)
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    seen = set()        # add seen island for every pot to avoid double count
                    candidate = 1       # the flip will add 1 to size of 2 island
                    for dr, dc in ((0,1),(1,0),(0,-1),(-1,0)):
                        nr = row+dr
                        nc = col+dc
                        if 0<=nr<n and 0<=nc<n:
                            iid = grid[nr][nc]
                            if iid>1 and iid not in seen:
                                candidate += island_size[iid]
                                seen.add(iid)
                    res = max(res,candidate)
        return res