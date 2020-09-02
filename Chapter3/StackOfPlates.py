class SetOfStacks:
    def __init__(self, cap):
        self.stacks = []
        self.cap = cap

    def push(self, item):
        # Push at the end of the list -> Check if curr stack has reached its cap
        if self.stacks and len(self.stacks[-1]) < self.cap:
            self.stacks[-1].append(item)
        else:
            # Create a new stack in the 'stacks'
            self.stacks.append([item])

    def pop(self):
        # Get rid of the empty stack within 'stacks', starting from the right
        while self.stacks and not len(self.stacks[-1]):
            self.stacks.pop()
        if not self.stacks:
            return None
        item = self.stacks[-1].pop()
        if not len(self.stacks[-1]):
            self.stacks.pop()
        return item

    # Given a stack number, pop() from there -> delete the most recent element from the stack at 'stack_num'
    def pop_at(self, stack_num):
        if stack_num < 0 or stack_num >= len(self.stacks):
            return None
        # The given stack @ 'stack_num' is empty
        if not len(self.stacks[stack_num]):
            return None
        return self.stacks[stack_num].pop()


if __name__ == '__main__':
    stack = SetOfStacks(3)
    stack.push(11)
    stack.push(22)
    stack.push(33)
    stack.push(44)
    stack.push(55)
    stack.push(66)
    stack.push(77)
    stack.push(88)
    assert(stack.pop()) == 88
    assert (stack.pop_at(1)) == 66
    assert (stack.pop_at(0)) == 33
    assert (stack.pop_at(1)) == 55
    assert (stack.pop_at(1)) == 44
    assert (stack.pop_at(1)) is None

    stack.push(99)

    assert (stack.pop()) == 99
    assert (stack.pop()) == 77
    assert (stack.pop()) == 22
    assert (stack.pop()) == 11
    assert (stack.pop()) is None
