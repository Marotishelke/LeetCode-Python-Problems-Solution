class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #--------------------------------------------------------------
        # Approach 2
        n=len(s)
        st={}
        ts={}
        for i in range(n):
            cs=s[i]
            ct=t[i]
            if cs not in st and ct not in ts:
                st[cs]=ct
                ts[ct]=cs
            elif cs in st and st[cs] != ct:  
                return False
            elif ct in ts and ts[ct] != cs: 
                return False
        return True
        #--------------------------------------------------------------

        #--------------------------------------------------------------
        # Approach 1
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
        #--------------------------------------------------------------
        
