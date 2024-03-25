class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # ----------------------------------------
        # Approach 2
        duplicate_lst = []
        size = len(nums)

        for idx in range(size):
            num = abs(nums[idx])
            idx = num - 1
            if nums[idx] < 0:
                duplicate_lst.append(num)
            nums[idx] *= -1
        return duplicate_lst
        # ----------------------------------------

        # ----------------------------------------
        # Approach 1
        duplicate_lst = []
        freq_nums = collections.Counter(nums)
        for num, freq in freq_nums.items():
            if freq >= 2:
                duplicate_lst.append(num)
        return duplicate_lst
        # ----------------------------------------
