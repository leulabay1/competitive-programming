class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.deque = [None]*self.k
        self.front = 0
        self.end = 0
        self.size = 0
        
    def insertFront(self, value: int) -> bool:
        if self.isEmpty():
            self.deque[self.front] = value
            self.size += 1
            return True
        elif not self.isFull():
            self.front = (self.front - 1) % self.k
            self.deque[self.front] = value
            self.size += 1
            return True
        else:
            return False
    def insertLast(self, value: int) -> bool:
        if self.isEmpty():
            self.deque[self.end] = value
            self.size += 1
            return True
        elif not self.isFull():
            self.end = (self.end + 1) % self.k
            self.deque[self.end] = value
            self.size += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.deque[self.front] = None
            if self.size != 1:
                self.front = (self.front + 1) % self.k
            self.size -= 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.deque[self.end] = None
            if self.size != 1:
                self.end= (self.end - 1) % self.k
            self.size -= 1
            return True
        else:
            return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.deque[self.front]
        else:
            return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.deque[self.end]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False
    def isFull(self) -> bool:
        if self.size != self.k:
            return False
        else:
            return True


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()