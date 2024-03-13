class Solution:
    def pivotInteger(self, n: int) -> int:

        # ---------------------------------------------------------------
        # Approach 2
        x = (n * (n + 1) / 2) ** 0.5

        if x % 1 != 0:
            return -1
        return int(x)
        # ---------------------------------------------------------------
       
        # ---------------------------------------------------------------
        # Approach 1
        """ if n == 1:
            return 1

        size = n
        pivot_ind = size // 2
        while(pivot_ind < size):
            sum_pivot = sum(range(1, pivot_ind+1))
            pivot_size_sum = sum(range(pivot_ind, size+1))

            print(sum_pivot, pivot_size_sum)

            if sum_pivot == pivot_size_sum:
                return pivot_ind    
            if sum_pivot < pivot_size_sum:
                pivot_ind += 1
            else:
                break
        return -1 """
        # ---------------------------------------------------------------
