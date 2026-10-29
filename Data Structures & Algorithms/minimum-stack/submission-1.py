class MinStack:

    def __init__(self):
        self.min = None
        self.stack = []
        self.secondary_stack = []
        
    def push(self, val: int) -> None:
        if self.min is None or val <= self.min:
            self.secondary_stack.append(self.min)
            self.min = val
        self.stack.append(val)

    def pop(self) -> None:
        res = self.stack.pop()
        if res == self.min:
            # self.secondary_stack.pop()
            self.min = self.secondary_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min
        
