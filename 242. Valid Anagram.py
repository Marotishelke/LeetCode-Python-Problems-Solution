from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ---------------------------------------------------
        # Approach 1
        if len(s) != len(t):
            return False
        s_dict = Counter(s)
        t_dict = Counter(t)
        for key in s_dict:
            if key in t_dict:
                if s_dict[key] != t_dict[key]:
                    return False
            else:
                return False
        return True 
    
        # ----------------------------------------------------

        # ----------------------------------------------------
        # Approach 2
        return sorted(s) == sorted(t)
        # -----------------------------------------------------

        # -----------------------------------------------------
        # Approach 3
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        
        for ch in t:
            freq[ord(ch) - ord('a')] -= 1
        
        for val in freq:
            if val != 0:
                return False
        return True
        # -----------------------------------------------------
