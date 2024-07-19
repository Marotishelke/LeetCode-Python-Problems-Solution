""" Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 105.
All elements in the matrix are distinct.
"""
class Solution:
    def luckyNumbers (self, mat: List[List[int]]) -> List[int]:
        # ----------------------------------------------------
        # Approach 2
        N, M = len(mat), len(mat[0])

        r_min_max = float('-inf')
        for i in range(N):
            r_min = min(mat[i])  
            r_min_max = max(r_min_max, r_min)

        c_max_min = float('inf')
        for i in range(M):
            c_max = max(mat[j][i] for j in range(N))
            c_max_min = min(c_max_min, c_max)

        if r_min_max == c_max_min:
            return [r_min_max]
        else:
            return []
        # ----------------------------------------------------

        # ----------------------------------------------------
        # Approach 1
        n = len(mat)
        m = len(mat[0])

        for i in range(n):
            minn = mat[i][0]
            min_index = 0

            for r in range(1, len(mat[i])):
                if mat[i][r] < minn:
                    minn = mat[i][r]
                    min_index = r
            
            maxx = minn   
            for c in range(0, len(mat)):
                if maxx < mat[c][min_index]:
                    maxx = mat[c][min_index]
   
            if minn == maxx:
                return [minn]
            # ----------------------------------------------------
