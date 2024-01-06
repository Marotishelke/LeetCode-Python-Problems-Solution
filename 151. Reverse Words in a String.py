class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.strip().split()
        ls.reverse()
        res = " ".join(ls)

        return res
