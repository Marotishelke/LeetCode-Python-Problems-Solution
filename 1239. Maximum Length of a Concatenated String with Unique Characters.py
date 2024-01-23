class Solution:
    def is_unique_chars(self, s):
        char_set = set()
        for c in s:
            if c in char_set:
                return False
            char_set.add(c)
        return True

    def dfs(self, arr, path, indx, result):
        if self.is_unique_chars(path):
            result[0] = max(result[0], len(path))

        if indx == len(arr) or not self.is_unique_chars(path):
            return 
        
        for i in range(indx, len(arr)):
            self.dfs(arr, path + arr[i], i + 1, result)

    def maxLength(self, arr: List[str]) -> int:
        result = [0]
        self.dfs(arr, "", 0, result)
        return result[0]
        
