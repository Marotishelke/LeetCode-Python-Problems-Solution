class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # Approach 1
        """
        if len(pref) <= 1:
            return pref
        
        res = pref[0]
        for ind in range(1, len(pref)):
            x = pref[ind]
            pref[ind] = res ^ pref[ind]
            res = x
        return pref
        """

        res_lst = []
        for i in range(len(pref)):
            if i == 0:
                res_lst.append(pref[i])
            else:
                res_lst.append(pref[i] ^ pref[i - 1])
        return res_lst
        
        
        
