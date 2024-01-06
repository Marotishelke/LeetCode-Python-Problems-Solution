class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        # -----------------------------------------------
        # Approach 1
        def cnt_ones(num):
            cnt = 0
            while(num):
                if num % 2 == 1:
                    cnt += 1
                num //= 2
            return cnt

        arr.sort()
        cnt_ones_arr = []

        for num in arr:
            cnt_ones_arr.append((num, cnt_ones(num)))
        
        cnt_ones = sorted(cnt_ones_arr, key= lambda x : x[1])
        
        return [key[0] for key in cnt_ones]
        # -----------------------------------------------

        # -----------------------------------------------
        # Approach 2
        arr.sort(key = lambda num: (bin(num).count('1'), num))
        return arr
        # -----------------------------------------------

        # -----------------------------------------------
        # Approach 3
        def count_ones(num):
            count = 0
            while num > 0:
                count += 1
                num &= (num - 1)
            return count
        
        arr.sort(key = lambda num : (count_ones(num), num))
        return arr
        # -----------------------------------------------
