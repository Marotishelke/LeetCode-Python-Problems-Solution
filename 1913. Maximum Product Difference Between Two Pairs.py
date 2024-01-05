import heapq
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # -----------------------------------------------------------
        # Approach 1
        largest, secondLargest = 0, 0
        smallest, secondSmallest = float('inf'), float('inf')

        for n in nums:
            if n < smallest:
                secondSmallest = smallest
                smallest = n
            elif n < secondSmallest:
                secondSmallest = n

            if n > largest:
                secondLargest = largest
                largest = n
            elif n > secondLargest:
                secondLargest = n

        return (largest * secondLargest) - (smallest * secondSmallest)
        # -----------------------------------------------------------

        # -----------------------------------------------------------
        # Approach 2
        largest, second_largest = heapq.nlargest(2, nums)
        smallest, second_smallest = heapq.nsmallest(2, nums)

        return (largest * second_largest) - (smallest * second_smallest)
        # -----------------------------------------------------------
