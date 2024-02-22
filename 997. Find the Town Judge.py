class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Count the number of people this guy is being trusted by.
        beingTrustedBy = defaultdict(int)

        # Count the number of people this guy trusts
        trusting = defaultdict(int)
        
        # Going through the trust relations.
        for a,b in trust:
            trusting[a] += 1
            beingTrustedBy[b] += 1
        
        # The judge trusting 0 people, and being trusted by n-1 people
        for i in range(1,n+1):
            if beingTrustedBy[i] == n-1 and trusting[i] == 0:
                return i
        
        # Didn't find a judge
        return -1
