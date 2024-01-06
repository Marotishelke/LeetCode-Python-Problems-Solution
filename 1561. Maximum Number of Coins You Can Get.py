class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        your_coin = 0
        for i in range(n // 3, n, 2):
            your_coin += piles[i]
        return your_coin        
