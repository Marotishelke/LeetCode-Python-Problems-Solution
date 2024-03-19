class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ##################################################################
        # Approach 1
        # Step 1: Count the frequncy of each task
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        # Sort the freuqncies 
        freq.sort()

        chunk = freq[25] - 1
        idle = chunk * n

        # Calculate number of intervals neede based on task.
        for i in range(24, -1, -1):
            idle -= min(chunk, freq[i])
        
        return len(tasks) + idle if idle >= 0 else len(tasks)
        ##################################################################
