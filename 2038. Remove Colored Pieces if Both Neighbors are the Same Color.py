class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # ------------------------------------------
        # Approach 1
        bob = 0
        alice = 0

        # Finding the moveing count
        for i in range(len(colors) - 2):
            if colors[i:i+3] == 'BBB':
                bob += 1
            if colors[i:i+3] == 'AAA':
                alice += 1

        # Checking Who moved more
        if alice > bob :
            return True
        else:
            return False
        # ------------------------------------------

        # ------------------------------------------
        # Approach 2
        c = collections.Counter()
        for key, value in groupby(colors):
            c[key] += max(len(list(value))-2, 0)
        
        if c['A'] > c['B']:
            return True
        return False
        # ------------------------------------------
