class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        # ----------------------Approach 2 --------------------------------
        m = len(matrix)
        n = len(matrix[0])

        transpose_matrix = [[0] * m for _ in range(n)]

        for col in range(n):
            for row in range(m):
                transpose_matrix[col][row] = matrix[row][col]
        return transpose_matrix
        # -----------------------------------------------------------------

        # ----------------------Approach 2 --------------------------------
        return zip(*matrix)
        # -----------------------------------------------------------------
