class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = deque([])
        self.ms = 0

    def next(self, val: int) -> float:
        self.ms += val
        if len(self.q) == self.size:
            self.ms -= self.q.popleft()
        self.q.append(val)
        return self.ms / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
