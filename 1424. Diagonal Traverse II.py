class Solution:

    # -------------------------------- Approach 1 --------------------------------
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        queue = deque([(0, 0)])
        ans = []

        while queue:
            row, col = queue.popleft()
            ans.append(nums[row][col])

            if col == 0 and row + 1 < len(nums):
                queue.append((row + 1, col))

            if col + 1 < len(nums[row]):
                queue.append((row, col + 1))
            
        return ans
    # -----------------------------------------------------------------------------

    # -------------------------------- Approach 2 ---------------------------------
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        for row in range(len(nums) - 1, -1, -1):
            for col in range(len(nums[row])):
                diagonal = row + col
                groups[diagonal].append(nums[row][col])
                
        ans = []
        curr = 0
        
        while curr in groups:
            ans.extend(groups[curr])
            curr += 1

        return ans
    # -----------------------------------------------------------------------------
