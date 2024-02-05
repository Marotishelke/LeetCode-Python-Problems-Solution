class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique_char_str = {}
        for charr in s:
            if charr not in unique_char_str:
                unique_char_str[charr] = 1
            else:
                unique_char_str[charr] += 1
        # print(unique_char_str)
        
        for i in range(len(s)):
            if unique_char_str[s[i]] == 1:
                return i
        return -1 
