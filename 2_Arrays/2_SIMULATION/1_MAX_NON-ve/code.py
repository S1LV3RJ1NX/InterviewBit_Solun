class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        max_sum = curr_sum = 0;
        startMax = endMax = -1;
        start = end = 0;
        
        while(end < len(A)):
            
            # if curr ele is greater than zero then continue
            if A[end] >= 0:
                
                # Add curr ele to sum
                curr_sum += A[end]
                
                # if currsum is greater than maxium sum calculated so far
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    
                    # Save it's start and end index. 
                    # we add 1 to end index as last index is exclusive
                    startMax = start;
                    endMax = end+1
                    
                elif curr_sum == max_sum:
                    # Comparing on length
                    if end-start+1 > endMax-startMax:
                        startMax = start
                        endMax = end + 1
            else:
                start = end+1
                curr_sum = 0
            end+=1
            
        if startMax == -1 or endMax == -1:
            return []
        return A[startMax:endMax]
        
    

