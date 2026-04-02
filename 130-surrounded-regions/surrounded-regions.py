class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        # for all the O connecting from the border make then # (safe)
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c]!="O":
                return
            board[r][c] = "#"
            dfs(r,c+1)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r-1,c)
    
        # first and last row
        for r in range(rows):
            dfs(r,0)
            dfs(r,cols-1)
        # first and last col
        for c in range(cols):
            dfs(0,c)
            dfs(rows-1,c)

        #  capute and revert all the safe cells
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c]="X"
                elif board[r][c] == "#":
                    board[r][c]="O"

        
        # # ["X","X","X","X"]
        # # ["X","O","X","X"]
        # # ["X","X","X","X"]
        # # ["X","O","X","X"]
        # rows = len(board)
        # cols = len(board[0])
        
        # def dfs(curr,parent):
        #     r,c = curr
        #     if r == 0 or c == 0 or r == rows-1 or c == cols-1:
        #         return False
        #     for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
        #         nr,nc = r+dr,c+dc
        #         if 0<nr<rows-1 and 0<nc<cols-1 and (nr,nc)!=parent and board[nr][nc] == "O":
        #             if dfs((nr,nc),(r,c)):
        #                 board[nr][nc] = "X"
        #     return True

        # # Skip
        # # def bfs(curr,parent)):
        # #     queue = deque([curr])
        # #     while queue:
        # #         r,c = queue.popleft()
        # #         for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
        # #             nr,nc = r+dr,c+dc
        # #             if 0<=nr<rows and 0<nc<cols and board[nr][nc] != "X" and 

        # for r in range(rows):
        #     for c in range(cols):
        #         if board[r][c]=="O":
        #             if dfs((r,c),(-1,-1)):
        #                 board[r][c]="X"
