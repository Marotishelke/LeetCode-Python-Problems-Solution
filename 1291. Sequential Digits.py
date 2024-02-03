class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # ---------------------------------------------------------------------------------------------------
        # Approach 1
        """
        1. Iterate through starting digits from 1 to 9.
        2. For each starting digit, build a sequential number by adding consecutive digits until reaching 9 or exceeding the high value.
        3. Add valid sequential numbers to a vector (a).
        4. Sort the vector.
        """
        a = []

        for i in range(1, 10):
            num = i
            next_digit = i + 1

            while num <= high and next_digit <= 9:
                num = num * 10 + next_digit
                if low <= num <= high:
                    a.append(num)
                next_digit += 1

        a.sort()
        return a     
        # ---------------------------------------------------------------------------------------------------   
