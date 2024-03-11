class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_dict = collections.Counter(s)
        b = ''
        
        for i in order:
            if i in s_dict:
                b += i * s_dict[i]
                s_dict.pop(i)
        

        for i in s_dict.keys():
            b += i * s_dict[i]
        return b
