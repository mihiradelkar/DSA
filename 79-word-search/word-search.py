class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        w = len(word)
        def backtrack(i,j,c):
            if c == w:
                return True
            if i<0 or i>=m or j<0 or j>=n:
                return False
            if word[c] != board[i][j]:
                return False
            board[i][j] = "#"
            # print(c, i, j, board[i][j])
            found =(backtrack(i,j+1,c+1) or 
                    backtrack(i+1,j,c+1) or 
                    backtrack(i,j-1,c+1) or 
                    backtrack(i-1,j,c+1))
            board[i][j] = word[c]
            return found

        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    if backtrack(i,j,0):
                        return True
        return False
        
        