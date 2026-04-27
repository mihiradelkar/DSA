class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # [[2,4,3],
        #  [6,5,2]]

        direction_map = {
            1:[(0,1),(0,-1)],
            2:[(1,0),(-1,0)],
            3:[(0,-1),(1,0)],
            4:[(0,1),(1,0)],
            5:[(0,-1),(-1,0)],
            6:[(0,1),(-1,0)],
        }
        m = len(grid)
        n = len(grid[0])
        queue = deque([(0,0)])
        visited = {(0,0)}
        
        while queue:
            r,c = queue.popleft()
            if r==m-1 and c ==n-1:
                return True
            # check what cells can we go
            for dr,dc in direction_map[grid[r][c]]:
                nr,nc = r+dr, c+dc
                # if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited:
                #     # print(nr,nc)
                #     # check if connected
                #     # for rdr, rdc in direction_map[grid[nr][nc]]:
                #     #     rnr,rnc = nr+rdr, nc+rdc
                #     #     # print(rnr,rnc)
                #     #     if r == rnr and c==rnc:
                #     #         queue.append((nr,nc))
                #     #         visited.add((nr,nc))
                #     #         break
                #     if (-dr,-dc) in direction_map[grid[nr][nc]]:
                #         queue.append((nr,nc))
                #         visited.add((nr,nc))
                if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited and (-dr,-dc) in direction_map[grid[nr][nc]]:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
                    
        return False