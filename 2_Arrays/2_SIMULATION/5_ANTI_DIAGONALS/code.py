# Refer:- https://www.careercup.com/question?id=5661939564806144
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
    
        ans = []
        ln = len(A[0])
        for D in range(2*ln-1):
            lis = []
            for i in range(D+1):
                if i<ln and (D-i)<ln:
                    lis.append(A[i][D-i])
            ans.append(lis)
            
        return ans
