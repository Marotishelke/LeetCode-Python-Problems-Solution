# import heapq
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Approach 1
        '''
        gain.insert(0, 0)
        for i in range(1, len(gain)):
            gain[i] = gain[i] + gain[i-1]
        return heapq.nlargest(1, gain)[0]
        '''

        # Approach 2
        current = 0
        highest = 0
        for value in gain:
            current += value
            highest = max(current, highest)
        return highest
