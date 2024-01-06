class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ''
        i = 0
        j = 0
        # Merging the alternative characters from both strings
        while(i < len(word1) and j < len(word2)):
            merged_string += word1[i] + word2[j]   
            i += 1
            j += 1
        
        # If word1 has more characters than word2
        while(i < len(word1)):
            merged_string += word1[i]
            i += 1
        
        # If word2 has more characters than word1
        while(j < len(word2)):
            merged_string += word2[j]
            j += 1
        return merged_string
