""" You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.

Example 1:

Input: rowSum = [3,8], colSum = [4,7]
Output: [[3,0],
         [1,7]]
Explanation: 
0th row: 3 + 0 = 3 == rowSum[0]
1st row: 1 + 7 = 8 == rowSum[1]
0th column: 3 + 1 = 4 == colSum[0]
1st column: 0 + 7 = 7 == colSum[1]
The row and column sums match, and all matrix elements are non-negative.
Another possible matrix is: [[1,2],
                             [3,5]]
Example 2:

Input: rowSum = [5,7,10], colSum = [8,6,8]
Output: [[0,5,0],
         [6,1,0],
         [2,0,8]]
 
Constraints:
1 <= rowSum.length, colSum.length <= 500
0 <= rowSum[i], colSum[i] <= 108
sum(rowSum) == sum(colSum)
"""
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # Approach 2
        N = len(rowSum)
        M = len(colSum)

        orig_matrix = [[0] * M for _ in range(N)]
        i, j = 0, 0

        while i < N and j < M:
            orig_matrix[i][j] = min(rowSum[i], colSum[j])

            rowSum[i] -= orig_matrix[i][j]
            colSum[j] -= orig_matrix[i][j]

            if rowSum[i] == 0:
                i += 1
            else:
                j += 1

        return orig_matrix

        # Approach 1
        N = len(rowSum)
        M = len(colSum)

        curr_row_sum = [0] * N
        curr_col_sum = [0] * M

        orig_matrix = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                orig_matrix[i][j] = min(
                    rowSum[i] - curr_row_sum[i], colSum[j] - curr_col_sum[j]
                )

                curr_row_sum[i] += orig_matrix[i][j]
                curr_col_sum[j] += orig_matrix[i][j]

        return orig_matrix
        
