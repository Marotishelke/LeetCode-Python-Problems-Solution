class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # ------------------------------------
        # Approach 1
        res_lst = []
        cnt = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[i] == words[j][::-1] and words[i] not in res_lst and words[i] not in res_lst:
                    cnt += 1
                    res_lst.append(words[i])
                    res_lst.append(words[i])
        return cnt
        # ------------------------------------

        # ------------------------------------
        # Approach 2
        d = defaultdict(int)

        for word in words:
            d[min(word, word[::-1])] += 1

        return sum(map((lambda x: x*(x-1)), d.values()))//2
        # ------------------------------------
        
