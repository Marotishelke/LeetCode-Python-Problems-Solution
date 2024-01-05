class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # ----------------------------------------------------
        # Approach 1
        ans = []
        temp = nums.copy()
        while(temp):
            lst = []
            print(len(temp))
            for i in range(len(temp)-1, -1, -1):
                if temp[i] not in lst:
                    lst.append(temp[i])
                    nums.pop(i)
            ans.append(lst)
            temp = nums
        return ans
        # ----------------------------------------------------

        # ----------------------------------------------------
        # Approach 2
        ans = []
        dd = collections.Counter(nums)
        maxx = max(dd.values())

        while maxx:
            sub_lst = []
            for key, val in dd.items():
                if val > 0:
                    sub_lst.append(key)
                    dd[key] -= 1
            ans.append(sub_lst)
            maxx -= 1
        return ans
        # ----------------------------------------------------

        # ----------------------------------------------------
        # Approach 3
        freq = [0] * (len(nums) + 1)
        ans = []

        for c in nums:
            if freq[c] >= len(ans):
                ans.append([])
            
            ans[freq[c]].append(c)
            freq[c] += 1
            # print(freq, ans)
        return ans
        # ----------------------------------------------------

        
