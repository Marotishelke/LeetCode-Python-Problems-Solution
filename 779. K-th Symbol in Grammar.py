class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Track if the values of k and first elemenets are same
        are_values_same = True

        """
            Calculate total number of elements in each row
            1st row :- 0  --->  1  
            2nd row :- 01 --->  2
            3rd row :- 0110 ---> 4
            4th row :- 01101001 ---> 8
            Formual = 2** (n-1)
        """
        n = 2 ** (n - 1)

        # Loop until we reach first row
        while n != 1:
            """
                Halve the number of elements in row
                If k in the second half of the row,
                adjust k and the flag
            """
            n //= 2
            if k > n:
                k -= n
                are_values_same = not are_values_same
        
        # Return 0 if flag shows the values are same. otherwise 1
        if are_values_same:
            return 0
        return 1
