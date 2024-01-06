class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        temp = ''
        for i in range(len(str1)):
            temp += str1[i]


            #Checking for Greatest Divisor
            if len(str1) % (i+1) == 0 and len(str2) % (i+1) == 0:
                #Multiply Greatest Divisor with Prefix String and check is it equal for both original string or not
                if temp * (len(str1) // (i+1)) == str1 and temp * (len(str2) // (i+1)) == str2:
                    res = temp
        return res
