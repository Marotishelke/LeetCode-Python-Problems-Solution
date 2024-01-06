from collections import *
class TimeMap:
    # -------------------------------------------------
    def __init__(self):
        self.cur_dict={}
    # -------------------------------------------------

    # -------------------------------------------------
    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.cur_dict:
            self.cur_dict[key]=[""]
        self.cur_dict[key].append([value,timestamp])
    # -------------------------------------------------
        
    # -------------------------------------------------
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cur_dict:
            return ""
        for i in range(len(self.cur_dict[key])-1,-1,-1):
            if self.cur_dict[key][i]=="":
                return ""
            x,y = self.cur_dict[key][i]
            if y<=timestamp:
                return x
    # -------------------------------------------------


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
