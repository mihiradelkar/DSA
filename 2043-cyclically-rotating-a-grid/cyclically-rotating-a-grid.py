class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # m = len(grid)
        # n = len(grid[0])
        # p = 2*(m+n)-4
        # k= k%p
        # layers = defaultdict(list)
        # for i in range(m):
        #     for j in range(n):
        #         layer = min(i%m, j%n)
        #         layers[layer].append(grid[i][j])
        # print(layers)
        # return grid

        m, n = len(grid), len(grid[0])
        for layer in range(min(m,n)//2):
            r1 = c1 = layer
            r2,c2 = m-1-layer,n-1-layer
            # make ring
            ring = []
            for c in range(c1,c2): ring.append(grid[r1][c])
            for r in range(r1,r2): ring.append(grid[r][c2])
            for c in range(c2,c1,-1): ring.append(grid[r2][c])
            for r in range(r2,r1,-1): ring.append(grid[r][c1])
            # shift
            l = len(ring)
            shift = k % l
            if shift == 0:
                continue
            ring = ring[shift:] + ring[:shift] 
            # put in grid
            idx = 0
            for c in range(c1,c2): grid[r1][c] = ring[idx]; idx+=1
            for r in range(r1,r2): grid[r][c2] = ring[idx]; idx+=1
            for c in range(c2,c1,-1): grid[r2][c] = ring[idx]; idx+=1
            for r in range(r2,r1,-1): grid[r][c1] = ring[idx]; idx+=1

        return grid
    