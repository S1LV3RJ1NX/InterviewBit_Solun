class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, arr):
        arr = list(arr)
        size = len(arr)
        for i in range(size): 
            if arr[abs(arr[i])-1] > 0: 
                arr[abs(arr[i])-1] = -arr[abs(arr[i])-1] 
            else: 
                rep = abs(arr[i])
                
              
        for i in range(size): 
            if arr[i]>0: 
                miss = i + 1
                
                
        return rep, miss
