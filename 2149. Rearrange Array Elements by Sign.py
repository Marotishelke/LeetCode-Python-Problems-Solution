class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        evenlst = [i for i in nums if i >0]
        oddlst = [i for i in nums if i < 0]
        print(evenlst,oddlst)
        res = []
        length = len(nums)
        j = 0
        while(j < (length // 2)):
            res.append(evenlst[j])
            res.append(oddlst[j])
            j += 1
        
        return res
