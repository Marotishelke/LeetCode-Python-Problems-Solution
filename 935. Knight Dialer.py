class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        v = [1] * 10

        for i in range(2, n + 1):
            tmp = [0] * 10
            for key, val in moves.items():
                for j in val:
                    tmp[key] = (tmp[key] + v[j]) % 1000000007
            v = tmp
        return sum(v) % 1000000007
        
