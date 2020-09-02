class MinStack:
    def __init__(self):
        self.stack = [(None, float('inf'))]

    def push(self, data):
        self.stack.append((data, min(data, self.stack[-1][1])))

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def get_min(self):
        return self.stack[-1][1]


# Space optimization: Maintain two independent stacks 'data' and 'min_data'
# Only update the 'min_data' stack when a smaller number is found
class MinStackOpt:
    def __init__(self):
        self.data = []
        self.min_data = [float('inf')]

    def push(self, val):
        if self.min_data and val < self.min_data[-1]:
            self.min_data.append(val)
        self.data.append(val)

    def pop(self):
        val = self.data.pop()
        if val == self.get_min():
            self.min_data.pop()
        return val

    def get_min(self):
        return self.min_data[-1] if self.min_data else None


if __name__ == '__main__':
    # my_stack = MinStack()
    # my_stack.push(5)
    # my_stack.push(6)
    # my_stack.push(2)
    # my_stack.push(7)
    # my_stack.push(14)
    # my_stack.push(3)
    # assert (my_stack.get_min()) == 2
    #
    # my_stack.push(1)
    # my_stack.push(4)
    # my_stack.push(44)
    # my_stack.push(2)
    # assert (my_stack.get_min()) == 1

    my_stack = MinStackOpt()
    my_stack.push(5)
    my_stack.push(6)
    my_stack.push(2)
    my_stack.push(7)
    my_stack.push(14)
    my_stack.push(3)
    assert (my_stack.get_min()) == 2

    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()

    assert (my_stack.get_min()) == 5

    my_stack.push(1)
    my_stack.push(4)
    my_stack.push(44)
    my_stack.push(2)
    assert (my_stack.get_min()) == 1


