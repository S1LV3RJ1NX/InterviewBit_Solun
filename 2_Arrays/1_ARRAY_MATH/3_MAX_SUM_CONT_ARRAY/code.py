class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        curr_sum = 0;
        
        max_found_until_now = A[0];
        for i in range(0,len(A)):
            curr_sum += A[i]
            
            if curr_sum < A[i]:
                curr_sum = A[i]
                
            if max_found_until_now < curr_sum:
                max_found_until_now = curr_sum
        
        return max_found_until_now