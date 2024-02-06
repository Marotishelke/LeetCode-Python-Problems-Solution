class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = collections.defaultdict(list)
        for strr in strs:
            word = ''.join(sorted(strr))
            anagram_dict[word].append(strr)
        
        return list(anagram_dict.values())
