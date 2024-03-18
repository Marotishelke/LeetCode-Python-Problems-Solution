class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        current_end = points[0][1]
        count = 1

        for start, end in points:
            if start > current_end:
                count += 1
                current_end = end
        return count
