class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:

        # --------------------------------
        # Approach 1
        def dec_bin(num):
            bin_ = 0
            cnt = 0 
            while(num > 0):
                rem = num % 2
                bin_ += rem  * (10 ** cnt)
                num //= 2
                cnt += 1
            return bin_

        sum_with_k_bits = 0
        for i in range(len(nums)):
            if str(dec_bin(i)).count('1') == k:
                print(str(dec_bin(i)), str(dec_bin(i)).count('1'))
                sum_with_k_bits += nums[i] 
        return sum_with_k_bits
        # --------------------------------

        # --------------------------------
        # Approach 2
        sum = 0
        for i in range(len(nums)):
            if bin(i)[2:].count('1') == k:
                sum += nums[i]

        return sum
        # --------------------------------
