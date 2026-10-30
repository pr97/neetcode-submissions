class Stack:
    def __init__(self):
        self.d = []
    def push(self, val):
        self.d.append(val)
    def pop(self):
        return self.d.pop()
    def top(self):
        return self.d[-1]
    def is_empty(self):
        return len(self.d) == 0

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = Stack()
        res = [0] * len(temperatures)
        for idx, t in enumerate(temperatures):
            if idx == 0:
                s.push((t, idx))
            else:
                if not s.is_empty():
                    if t <= s.top()[0]:
                        s.push((t, idx))
                    else:
                        while not s.is_empty() and t > s.top()[0]:
                            item = s.pop()
                            res[item[1]] = idx - item[1]
                        s.push((t, idx))
        return res