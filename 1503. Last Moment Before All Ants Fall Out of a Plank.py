class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = 0
        for num in left:
            ans = max(ans, abs(0 - num))
        
        for num in right:
            ans = max(ans, abs(n - num))
        
        return ans
