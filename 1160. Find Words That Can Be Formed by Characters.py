class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        good_string_length = 0
        for word in words:
            flag = 1
            for char in word:
                if word.count(char) > chars.count(char):
                    flag = 0
                    break
            if flag:
                good_string_length += len(word)
        return good_string_length
