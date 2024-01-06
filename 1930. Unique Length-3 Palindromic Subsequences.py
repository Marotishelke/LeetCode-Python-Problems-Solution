class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # ----------------------------------------
        # Approach 1 (Time Exceeded)
        """ cnt = 0
        length = len(s)
        lst = []
        for i in range(length-2):
            for j in range(i+1, length-1):
                for k in range(j+1, length):
                    string = s[i] + s[j] + s[k]
                    sorted_str = sorted(string)
                    if string == string[::-1] and sorted_str not in lst:
                        cnt += 1
                        lst.append(sorted_str)
        return cnt
        """
        # ----------------------------------------

        # ----------------------------------------
        # Approach 2
        res = 0
        unique = set(s)

        for char in unique:
            start = s.find(char) # Search character from left(start)
            end = s.rfind(char) # Search charcter from right (end)

            if start < end:
                res += len(set(s[start+1:end]))
        return res
        # ----------------------------------------

        # ----------------------------------------
        # Approach 3
        # Set to store unique palidromes
        unique_palindromes = set()

        # Dictionary to store the first and last index of each character
        char_indices = {}

        # Populate the dictionary with the first and last indices of each character
        for i, char in enumerate(s):
            if char not in char_indices:
                char_indices[char] = [i, i]
            else:
                char_indices[char][1] = i
        
        # Iterate through each character
        for char, indices in char_indices.items():
            # If the character occurs more than once
            if indices[0] < indices[1]:
                # Add all unique characters between first and last occurrence of 'char'
                unique_palindromes.update({char + mid_char + char for mid_char in set(s[indices[0] + 1:indices[1]])})
        return len(unique_palindromes)
    # ----------------------------------------
