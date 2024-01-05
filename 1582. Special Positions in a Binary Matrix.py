class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        # ----------------------- Approach 1 ----------------------------
        def get_col_sum(col_ind):
            return sum(row[col_ind] for row in mat)
        
        ans = 0
        for row in mat:
            if sum(row) == 1:
                col_ind = row.index(1)
                ans += get_col_sum(col_ind) == 1
        return ans
        # ---------------------------------------------------------------

        # ----------------------- Approach 2 ----------------------------
        cnt = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    continue

                flag = True
                for r in range(len(mat)):
                    if mat[r][col] == 1 and row != r:
                        flag = False
                        break
                
                for c in range(len(mat[0])):
                    if mat[row][c] == 1 and col != c:
                        flag = False
                        break
                
                if flag:
                    cnt += 1
        return cnt

        # ---------------------------------------------------------------
                

        

        
