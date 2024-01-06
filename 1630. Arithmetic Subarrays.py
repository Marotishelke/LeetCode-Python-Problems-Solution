class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        ans = []
        m = len(l)

        for i in range(m):
            v = nums[l[i]:r[i] + 1]
            v.sort()
            is_arith = True
            if len(v) > 1:
                diff = v[1] - v[0]
                for j in range(1, len(v)):
                    if v[j] - v[j - 1] != diff:
                        is_arith = False
                        break
            else:
                is_arith = False
            ans.append(is_arith)

        return ans
