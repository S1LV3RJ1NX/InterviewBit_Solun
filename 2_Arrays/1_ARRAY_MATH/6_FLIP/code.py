class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        max_diff = 0
        diff = 0
        ones = 0
        start = 0
        ans = None
		
		# enumerate gives two values i-> index of element , a->element itself
        for i, a in enumerate(A):
       	# Main logic starts here
            diff += (1 if a is '0' else -1)

            if diff < 0:
                diff = 0
                start = i + 1
                continue

            if diff > max_diff:
                max_diff = diff
                # Create list of start and end index
                ans = [start, i]

        if ans is None:
            return []
        # Logic ends here
           
        # Just pythonic way of adding +1 to both index
        return map(lambda x: x + 1, ans)

