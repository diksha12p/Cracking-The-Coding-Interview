class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not len(self.stack):
            return None
        return self.stack.pop()

    def __len__(self):
        return len(self.stack)


class QueueViaStack:
    def __init__(self):
        self.stack_new = Stack()
        self.stack_old = Stack()

    def add(self, val):
        self.stack_new.push(val)

    def remove(self):
        # Updating the stack_old to have the most recent elements
        if not len(self.stack_old):
            while len(self.stack_new):
                self.stack_old.push(self.stack_new.pop())
        return self.stack_old.pop()


if __name__ == '__main__':
    queue = QueueViaStack()
    queue.add(11)
    queue.add(22)
    queue.add(33)

    assert (queue.remove()) == 11

    queue.add(44)
    queue.add(55)
    queue.add(66)
    
    assert (queue.remove()) == 22
    assert (queue.remove()) == 33
    assert (queue.remove()) == 44
    assert (queue.remove()) == 55

    queue.add(77)

    assert (queue.remove()) == 66
    assert (queue.remove()) == 77
    assert (queue.remove()) is None




