class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        
        length = len(A)
        carry = 0
        
        A[-1] = A[-1]+1+carry;
        carry = A[-1] // 10;
        A[-1] = A[-1] % 10;
       
        
        for i in range(length-2,-1,-1):
            A[i] = A[i]+carry;
            carry = A[i] // 10;

            A[i] = A[i] % 10;
            if carry == 0:
                break;
            
        if carry>0:
            A.insert(0,carry)
            
        while A[0] == 0:
            A.pop(0)
            
        return A
