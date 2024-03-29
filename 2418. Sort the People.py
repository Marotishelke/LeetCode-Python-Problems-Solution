class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        lst =  list(zip(names, heights))
        lst.sort(key = lambda tup:tup[1], reverse=True)
        return [name[0] for name in lst]
