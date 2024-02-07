class Solution:
    def frequencySort(self, s: str) -> str:
        
        # ---------------------------------------------------------------------------------
        # Approach 1   T.C - O(nlogn)   S.C - O(n)
        # Frequency of each character store in dictionary 
        freq_char_heap = collections.Counter(s)

        # Sort the freq char dictionary using values (frequency) descending order
        freq_sorted_char = sorted(freq_char_heap.items(), key = lambda x: x[1], reverse=True)

        # Merge the sorted list with char and it's frequency
        sorted_char_by_freq = ''.join([key*value for key, value in freq_sorted_char])

        return sorted_char_by_freq
        # ---------------------------------------------------------------------------------
        

        # ---------------------------------------------------------------------------------
        # Approach 2   T.C - O(n)  S.C - O(n)
        # Frequency of each character store in dictionary
        freq_char_heap = collections.Counter(s)

        # Find max frequency 
        max_freq = max(freq_char_heap.values())

        # Create container of max frequnecy size to store characters frequency wise
        freq_char_container = [[] for _ in range(max_freq + 1)]

        # Append characters based on frequnecy in freq_char_container
        for char, freq in freq_char_heap.items():
            freq_char_container[freq].append(char)
        print(freq_char_container)
        
        result = ''
        for freq in range(max_freq, 0, -1):
            result += ''.join([char * freq for char in freq_char_container[freq]])
        return result
        # ---------------------------------------------------------------------------------
