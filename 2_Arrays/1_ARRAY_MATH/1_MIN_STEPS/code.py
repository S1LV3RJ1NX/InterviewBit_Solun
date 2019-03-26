class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        
        length = len(A)
        steps = 0
        for i in range(length-1):
            x = abs(A[i]-A[i+1])
            y = abs(B[i]-B[i+1])
            
            steps += max(x,y)
            
        return steps
