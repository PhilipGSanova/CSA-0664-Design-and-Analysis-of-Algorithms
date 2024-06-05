from collections import OrderedDict

class FirstUnique:
    def __init__(self, nums):
        self.queue = OrderedDict()
        self.unique_nums = {}
        for num in nums:
            self.add(num)
    
    def showFirstUnique(self):
        if self.queue:
            return next(iter(self.queue.values()))
        return -1
    
    def add(self, value):
        if value in self.unique_nums:
            if self.unique_nums[value]:
                self.queue.pop(value)
                self.unique_nums[value] = False
        else:
            self.queue[value] = value
            self.unique_nums[value] = True
