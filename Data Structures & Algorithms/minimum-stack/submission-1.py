class MinStack_naive:

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


class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:

        # If there are no values in the stack, first init
        if not self.stack:
            self.stack.append(0)
            self.min = val
        # Add the new value. If min, make the min
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val
        
    def pop(self) -> None:
        if not self.stack:
            return
        
        # Gets element on top of stack
        pop = self.stack.pop()
        
        # If that element was the minimum, restore old min
        if pop < 0:
            self.min = self.min - pop
        

    def top(self) -> int:
        top = self.stack[-1]
        
        # Restore encoded value before returning
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min

