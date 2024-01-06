class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_dict = collections.Counter(nums)
        n = len(nums)
        return [key for key in count_dict if count_dict[key] > (n/3)]
