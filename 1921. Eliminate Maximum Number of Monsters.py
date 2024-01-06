from math import ceil
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # ----------------------------------------
        # Approach 1
        # Calculated arrived times

        time_to_city = [dist[i] / speed[i] for i in range(len(dist))]
        time_to_city.sort()

        for i in range(len(time_to_city)):
            if time_to_city[i] <= i:
                return i
        return len(dist)
        # ----------------------------------------

        # ----------------------------------------
        # Approach 2
        n = len(dist)
        for i in range(n):
            dist[i] = ceil(dist[i] / speed[i]) # calculate the arrival times
            speed[i] = 0
        
        for num in dist:
            if num >= n:
                continue
            speed[num] += 1
        
        for i in range(1, len(speed)):
            speed[i] += speed[i - 1]
            if speed[i] > i:
                return i
        return n
        # ----------------------------------------
