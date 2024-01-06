class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest_no_candies = heapq.nlargest(1, candies)[0]
        return [True if candy + extraCandies >= greatest_no_candies else False for candy in candies]
