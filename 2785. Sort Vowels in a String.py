class Solution:
    def sortVowels(self, s: str) -> str:
        # Collect vowels and sort it
        vowels_sorted = sorted([char for char in s if char.lower() in 'aeiou'], reverse=True)

        # Create ans string by replacing vowels in sorted order\
        res = []
        for char in s:
            if char.lower() in 'aeiou':
                res.append(vowels_sorted.pop())
            else:
                res.append(char)
        
        # Join list as string format
        return ''.join(res)        
