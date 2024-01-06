class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # Approach 1
        """
        Step 1 : Finding the max index of garbage
        Step 2 : Taking the sum of time to reach max index of garbage
        Step 3 : Add count of garbage into sum (beacuse for picking it takes 1 min)
        Step 4 : Repeat above steps for each garbage  
        """

        amount_of_time = 0
        for gbage in ['M', 'G', 'P']:
            time = 0
            for i in range(len(garbage), -1, -1):
                if gbage in garbage[i-1]:
                    time = time + sum(travel[:i-1]) + (''.join(garbage)).count(gbage)
                    break
            amount_of_time += time
        return amount_of_time
