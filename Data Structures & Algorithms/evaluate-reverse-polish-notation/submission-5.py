class Stack:
    def __init__(self):
        self.d = []
    def push(self, val):
        self.d.append(val)
    def pop(self):
        return self.d.pop()
    def top(self):
        return self.d[-1]

class Solution:
    def is_op(self, val):
        return val in ['+', '-', '*', '/']

    def operate(self, a, b, op):
        a = int(a)
        b = int(b)
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            res = abs(a) // abs(b)
            if a * b < 0:
                return -res
            else:
                return res
            
    
    def evalRPN(self, tokens: List[str]) -> int:
        s = Stack()
        for token in tokens:
            if not self.is_op(token):
                s.push(token)
            else:
                b = s.pop()
                a = s.pop()
                res = self.operate(a, b, op=token)
                s.push(res)
        return int(s.pop())