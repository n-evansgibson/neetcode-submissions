class MinStack:

    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        item = self.stack[-1]
        del self.stack[-1]
        return item
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
        
