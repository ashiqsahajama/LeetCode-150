class RandomizedSet:

    def __init__(self):
        self.obj = []
        self.dict = {}
        

    def insert(self, val: int) -> bool:
        if self.dict.get(val)!=None:
            return False
        else:
            self.obj.append(val)
            self.dict[val]=len(self.obj)-1
            return True
        

    def remove(self, val: int) -> bool:
        if self.dict.get(val)!=None:
            last = self.obj[-1]
            rem = self.dict[val]
            self.obj[rem]=last
            self.dict[last]=rem
            self.obj.pop()
            del self.dict[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return choice(self.obj)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
