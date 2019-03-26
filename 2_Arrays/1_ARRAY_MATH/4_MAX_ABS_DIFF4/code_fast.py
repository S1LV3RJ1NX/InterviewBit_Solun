class Solution:
	# @param A : list of integers
	# @return an integer
	def maxArr(self, A):
	    result = 0
	    first = [A[i]+i for i in range(len(A))]
	    second = [A[i]-i for i in range(len(A))]
	    first_min, first_max = min(first), max(first)
	    second_min, second_max = min(second), max(second)
	    return max(first_max - first_min, second_max - second_min)
