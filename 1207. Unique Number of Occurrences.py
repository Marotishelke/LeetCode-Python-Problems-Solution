class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # --------------------------------------------------
        # Approach 1 O(nlog(n))
        # --------------------------------------------------
        """ arr_dict = collections.Counter(arr)
        freq_lst = list(arr_dict.values())
        for freq in freq_lst:
            if freq_lst.count(freq) > 1:
                return False
        return True
        """

        # --------------------------------------------------
        # Approach 2 O(n)
        # --------------------------------------------------
        freq = collections.Counter(arr)

        return len(freq) == len(set(freq.values()))
