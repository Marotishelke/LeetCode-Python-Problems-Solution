class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = 1
        suffix_product = 1
        result_product = [True]*len(nums)

        # Find the prefix product and store in result list
        for i in range(len(nums)):
            result_product[i] = prefix_product
            prefix_product *= nums[i]
        print(result_product)
        
        # Multple through suffix
        for i in range(len(nums)-1, -1, -1):
            result_product[i] *= suffix_product
            suffix_product *= nums[i]
        return result_product
