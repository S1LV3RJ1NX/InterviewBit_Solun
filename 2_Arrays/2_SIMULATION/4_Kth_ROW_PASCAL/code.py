# Refer:- https://stackoverflow.com/a/19856661/7420713
class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        
        ans = [1]
        
        for i in range((A//2)):
            ans.append(ans[i] * (A-i) // (i+1))
            
        for i in range((A//2)+1, A+1):
            ans.append(ans[A-i])
            
        return ans
