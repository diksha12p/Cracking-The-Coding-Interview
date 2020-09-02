class FixedMultiStack:
    def __init__(self, stack_size):
        self.num_stacks = 3
        self.arr = [0] * (stack_size * self.num_stacks)
        self.sizes = [0] * self.num_stacks
        self.stack_size = stack_size

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_size

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def push(self, item, stack_num):
        if self.is_full(stack_num):
            raise Exception('Stack Overflow!')
        self.sizes[stack_num] += 1
        self.arr[self.curr_top_index(stack_num)] = item

    def curr_top_index(self, stack_num):
        return self.sizes[stack_num] - 1 + (stack_num * self.stack_size)

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception('Stack Underflow!')
        return self.arr[self.curr_top_index(stack_num)]

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception('Stack Underflow!')
        old_val = self.arr[self.curr_top_index(stack_num)]
        self.arr[self.curr_top_index(stack_num)] = 0
        self.sizes[stack_num] -= 1
        return old_val


if __name__ == '__main__':
    new_stack = FixedMultiStack(2)
    assert (new_stack.is_empty(1)) is True
    new_stack.push(3, 1)
    assert (new_stack.peek(1)) == 3
    assert (new_stack.is_empty(1)) is False
    new_stack.push(2, 1)
    assert (new_stack.peek(1)) == 2
    assert (new_stack.pop(1)) == 2
    assert (new_stack.peek(1)) == 3
    new_stack.push(3, 1)




