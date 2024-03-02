class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square_lst = list(map(lambda x: x**2, nums))
        square_lst.sort()
        return square_lst
