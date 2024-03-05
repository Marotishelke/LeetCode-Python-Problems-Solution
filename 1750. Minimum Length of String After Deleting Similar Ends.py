class Solution:
    
    """# -----------------------------------------------------------------------------------
    def minimumLength(self, s: str) -> int:

        # Approach 1
        prefix_ptr = 0
        suffix_ptr = len(s) - 1

        # Delete similar ends until the ends differ or they meet in the middle
        while(prefix_ptr < suffix_ptr):
            if s[prefix_ptr] == s[suffix_ptr]:

                # Delete consecutive occurrences of c from prefix
                while((prefix_ptr < suffix_ptr and s[prefix_ptr] == s[prefix_ptr + 1])):
                    prefix_ptr += 1
                
                # Delete consecutive occurrences of c from suffix
                while((prefix_ptr < suffix_ptr and s[suffix_ptr] == s[suffix_ptr - 1])):
                    suffix_ptr -= 1
                
                prefix_ptr += 1
                suffix_ptr -= 1
            
            else:
                break
        
        # Return the number of remaining characters
        ans = suffix_ptr - prefix_ptr + 1
        if ans < 0:
            return 0
        return ans
    # -----------------------------------------------------------------------------------
    """

    # -----------------------------------------------------------------------------------
    # Approach 2
    def minimumLength(self, s: str) -> int:
        return self.delete_similar_ends(s, 0, len(s) - 1)

    # Deletes similar ends and returns remaining length
    def delete_similar_ends(self, s: str, begin: int, end: int) -> int:
        # The ends differ or meet in the middle
        if begin >= end or s[begin] != s[end]:
            return end - begin + 1
        else:
            c = s[begin]
            
            # Delete consecutive occurrences of c from prefix
            while begin <= end and s[begin] == c:
                begin += 1

            # Delete consecutive occurrences of c from suffix
            while end > begin and s[end] == c:
                end -= 1

            return self.delete_similar_ends(s, begin, end)
    # -----------------------------------------------------------------------------------
