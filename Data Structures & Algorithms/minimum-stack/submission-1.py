class MinStack:

    def __init__(self):
        self.stack = []
        self.w = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.w:
            val = min(val, self.w[-1])
        self.w.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.w.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.w[-1]