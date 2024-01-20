class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # -------------------------------------------------------------
        MODULO = 10 ** 9 + 7
        stack = []
        sum_of_min_nums = 0

        for i in range(len(arr) + 1):
            while(stack and (i == len(arr) or arr[stack[-1]] >= arr[i])):
                mid = stack.pop()
                left_bound = stack[-1] if stack else -1
                right_bound = i

                count = ((mid - left_bound) * (right_bound - mid)) % MODULO

                sum_of_min_nums += (count * arr[mid]) % MODULO

                sum_of_min_nums %= MODULO
            stack.append(i)

        return int(sum_of_min_nums)
        # -------------------------------------------------------------


        # -------------------------------------------------------------
        # Approach 1 (Time Limit Exceeded)
        """ slicing_window = 1
        MODULO = ((10 ** 9) + 7)
        stack = []
        for i in range(len(arr)):
            for j in range(len(arr)):
                if j + slicing_window <= len(arr):
                    stack.append(min(arr[j:j + slicing_window]))
                else:
                    break
            slicing_window += 1
        
        return sum(stack) % MODULO
        """
        # -------------------------------------------------------------
