# 981. Time Based Key-Value Store
# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.Dict = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.Dict:
            self.Dict[key].append((value, timestamp))
        else:
            self.Dict[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.Dict or timestamp < self.Dict[key][0][1]:
            return ""
        l = 0
        r = len(self.Dict[key]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if self.Dict[key][mid][1] == timestamp:
                return self.Dict[key][mid][0]
            elif self.Dict[key][mid][1] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        
        # if target was not in the array, return the right pointer as it will 
        # always be equal to the smaller value (that we want) as the r and l 
        # pointers converge and cross each other
        return self.Dict[key][r][0]       

    def printMap(self):
        print(self.Dict)

if __name__ == "__main__":

    timeMap = TimeMap()
    timeMap.set("a", "bar", 1)
    timeMap.set("x", "b", 3)
    print(timeMap.get("b", 3))
    timeMap.set("foo","bar2", 4)
    print(timeMap.get("foo", 4))
    print(timeMap.get("foo", 5))
    
    timeMap.set("love","high", 10)
    timeMap.set("love","low", 20)
    print(timeMap.get("love",5))

    timeMap.set("foo", "bar", 1)
    timeMap.set("foo", "bar2", 3)
    timeMap.set("foo", "bar3", 7)
    timeMap.set("foo", "bar4", 9)
    timeMap.set("foo", "bar5", 13)
    timeMap.set("foo", "bar6", 15)
    print(timeMap.get("foo", 14))

    timeMap.set("foo", "bar", 1)    
    print(timeMap.get("foo", 1))        # bar
    print(timeMap.get("foo", 3))        # bar
    timeMap.set("foo", "bar2", 4)       
    print(timeMap.get("foo", 4))        # bar2
    print(timeMap.get("foo", 5))        # bar2

