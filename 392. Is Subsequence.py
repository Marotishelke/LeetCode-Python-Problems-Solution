class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # --------------------------------------------------
        # Approach 1
        ind = 0
        cnt = 0
        # checking substring is found in main string or not substring must follow the order in Main string as well
        for i in s:
            while(ind < len(t)):
                if i == t[ind]:
                    cnt += 1
                    ind += 1
                    break
                ind += 1
        if len(s) == cnt:
            return True
        else:
            return False
        # --------------------------------------------------

        # --------------------------------------------------
        # Approach 2
        i = 0
        j = 0
        while(i < len(s) and j < len(t)):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
                
        return True if i == len(s) else False
        # --------------------------------------------------
