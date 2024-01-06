class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        """ Find the radius from the point
            Then check the radius is less than or equal to the radius which in queries
            """

        ans = []
        for circle in queries:
            no_points = 0
            for point in points:
                radius = (((circle[0] - point[0]) ** 2) + ((circle[1] - point[1]) ** 2)) ** 0.5
                if radius <= circle[2]:
                    no_points += 1
            ans.append(no_points)
        return ans
