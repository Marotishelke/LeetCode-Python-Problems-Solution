class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = []
        for i in range(numRows):
            sub_lst = []
            for j in range(i+1):
                if j == 0:
                    sub_lst.append(1)
                elif j == i:
                    sub_lst.append(1)
                else:
                    sub_lst.append(dp[i-1][j-1] + dp[i-1][j])
            dp.append(sub_lst)
        return dp
