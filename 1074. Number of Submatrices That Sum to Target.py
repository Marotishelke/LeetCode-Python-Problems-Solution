class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        for row in range(m):
            for col in range(1, n):
                matrix[row][col] += matrix[row][col - 1]

        count = 0
        
        for col1 in range(n):
            for col2 in range(col1, n):
                prefix_sum_count = {0: 1}
                sum_val = 0

                for row in range(m):
                    sum_val += matrix[row][col2] - (matrix[row][col1 - 1] if col1 > 0 else 0)
                    count += prefix_sum_count.get(sum_val - target, 0)
                    prefix_sum_count[sum_val] = prefix_sum_count.get(sum_val, 0) + 1
        return count
