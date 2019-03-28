# Refer Method 3:- https://www.geeksforgeeks.org/pascal-triangle/ 
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        
        ans = []
        
        for line in range(1, A+1):
            C = 1;
            lis = []
            for i in range(1, line+1):
                lis.append(C)
                C = int(C*(line-i)/i)
                
            ans.append(lis)
            
        return ans
        

