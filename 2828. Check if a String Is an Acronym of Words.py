class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        length = len(s)
        if(len(words) != len(s)):         # If String and list doesn't have same length
            return False

        for i in range(length):
            if words[i][0] != s[i]:       # If first character is not maches
                return False
        return True
