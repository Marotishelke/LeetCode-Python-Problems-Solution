class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_integer = ''
        for i in range(2, len(num)):
            if num[i] == num[i-1] and num[i-1] == num[i - 2] and good_integer < num[i-2:i+1]:
                good_integer = num[i-2:i+1]
        return good_integer
