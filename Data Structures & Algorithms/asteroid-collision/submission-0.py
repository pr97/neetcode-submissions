class Stack:
    def __init__(self):
        self.s = []
    
    def push(self, val):
        self.s.append(val)
    
    def pop(self):
        return self.s.pop()

    def top(self):
        if len(self.s) > 0:
            return self.s[-1]
        else:
            raise IndexError

    def __len__(self):
        return len(self.s)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = Stack()
        for a in asteroids:
            if len(s) == 0:
                s.push(a)
            else:
                current_destroyed = False
                while len(s) > 0 and s.top() > 0 and a < 0:
                    if abs(s.top()) == abs(a):
                        current_destroyed = True
                        s.pop()
                        break
                    if abs(s.top()) > abs(a):
                        current_destroyed = True
                        break
                    if abs(s.top()) < abs(a):
                        s.pop()
                if not current_destroyed:
                    s.push(a)

        return s.s
            
