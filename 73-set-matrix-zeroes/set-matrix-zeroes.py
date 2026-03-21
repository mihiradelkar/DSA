class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        # rows = set()
        # cols = set()
        # for row in range(m):
        #     for col in range(n):
        #         if matrix[row][col]==0:
        #             rows.add(row)
        #             cols.add(col)
        
        # for row in range(m):
        #     for col in range(n):
        #         if row in rows or col in cols:
        #             matrix[row][col]=0

        first_row = False
        first_col = False
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col]==0:     # if 0 found
                    if row == 0:            # is it in the first row?
                        first_row = True    # flag to make entire row 0
                    if col == 0:            # is it in the first col?
                        first_col = True    # flag to make entire col 0
                    matrix[row][0]=0        # make 0 in first row
                    matrix[0][col]=0        # make 0 in first col
        
        # make the inner box values 0 if 0th row/col has a 0 
        for row in range(1,m):
            for col in range(1,n):
                if matrix[row][0]==0 or matrix[0][col]==0:
                    matrix[row][col]=0
        
        # if first row had a 0 iterate over 1st col to make entire col 0
        if first_row:
            for col in range(n):
                matrix[0][col]=0
        
        # if first col had a 0 iterate over 1st row to make entire row 0
        if first_col:
            for row in range(m):
                matrix[row][0]=0
