class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        # Approach 1
        """ Step 1:- Use two loops outer for row and inner for column
            Step 2:- Take Sum of current row for finding count of 1 and
                      Take substraction to take count of 0's
            Step 3:- Create function to take the sum of the col and Same
                     thing follow as in followed in step 2.
            Step 4:- Take the sum of 1's count and substract the sum of 0's
                     count
        """
        # ----------------------------------------------------------------------
        """
        n = len(grid)  # Number of rows
        m = len(grid[0]) # Number of columns

        diff_grid = [[0 for i in range(m)] for j in range(n)]

        def get_col_sum(col_ind):
            return sum([grid[i][col_ind] for i in range(n)])

        for row in range(n):
            for col in range(m):
                print(sum(grid[row]), get_col_sum(col))
                diff_grid[row][col] = ((sum(grid[row]) - abs(m - sum(grid[row]))) + (get_col_sum(col) - abs(n - get_col_sum(col))))
        return diff_grid
        """
        # --------------------------------------------------------------------------

        #------------------------------------------------------------------------------
        # Approach 2
        m, n = len(grid), len(grid[0])

        row_ones = [0] * m
        col_ones = [0] * n

        # Count ones in each row and column
        for i in range(m):
            for j in range(n):
                row_ones[i] += grid[i][j]
                col_ones[j] += grid[i][j]

        # Calculate the difference matrix
        for i in range(m):
            for j in range(n):
                grid[i][j] = 2 * (row_ones[i] + col_ones[j]) - m - n

        return grid
                            
                        
        
