class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_num_dict = collections.Counter(arr)
        freq_num_lst = sorted(freq_num_dict.items(), key = lambda item: item[1])

        len_counter = len(freq_num_lst)

        for mat in freq_num_lst:
            if mat[1] <= k:
                k -= mat[1]
                len_counter -= 1
            else:
                break
        return len_counter
