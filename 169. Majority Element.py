class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # ---------------------------------------
        """
        # Approach 1 (TLE)
        length = len(nums)

        for i in range(length):
            cnt_freq_num = 1
            for j in range(i+1, length):
                if nums[i] == nums[j]:
                    cnt_freq_num += 1
            
            if cnt_freq_num > length // 2:
                return nums[i]
        """
        # ---------------------------------------

        # ---------------------------------------
        # Approach 2
        length = len(nums)

        freq_num_dict = {}
        for num in nums:
            if num in freq_num_dict:
                freq_num_dict[num] += 1
            else:
                freq_num_dict[num] = 1
        
        for num, freq in freq_num_dict.items():
            if freq > length // 2:
                return num
        # ---------------------------------------

        # ---------------------------------------
        # Approach 3
        import collections
        length = len(nums)

        freq_num_dict = collections.Counter(nums)

        for num, freq in freq_num_dict.items():
            if freq > length // 2:
                return num
        # ---------------------------------------
