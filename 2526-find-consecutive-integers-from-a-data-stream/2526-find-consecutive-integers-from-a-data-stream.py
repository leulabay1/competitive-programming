class DataStream:

    def __init__(self, value: int, k: int):
        self.streams = []
        self.value = value
        self.k = k
        self.freq = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.freq += 1
        else:
            self.freq = 0
        return True if self.freq >= self.k else False
            


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)