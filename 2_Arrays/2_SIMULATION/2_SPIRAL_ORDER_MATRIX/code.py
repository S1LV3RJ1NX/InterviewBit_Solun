class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        
        mat = [[0 for j in range(A)] for i in range(A)]
        
        row_start = col_start = 0;
        row_end = col_end = A-1;
        curr = 1;
        
        while row_start<= row_end and col_start<=col_end:
            
            # top row, left->right
            for c in range(col_start, col_end+1):
                mat[row_start][c] = curr;
                curr+=1
            row_start +=1
            
            # last col, top->bottom
            for r in range(row_start, row_end+1):
                mat[r][col_end] = curr
                curr+=1
            col_end -= 1
            
            # last row, right->left
            for c in range(col_end, col_start-1,-1):
                mat[row_end][c] = curr
                curr+=1
            row_end -= 1
            
            # fst col, bottom->top
            for r in range(row_end, row_start-1,-1):
                mat[r][col_start] = curr
                curr+=1
            col_start+=1
            
        return mat
        

