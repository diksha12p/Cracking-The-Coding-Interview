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

    def print_stack(self):
        while self.stack:
            print(self.stack.pop(), end=" ")

    def peek(self):
        return self.stack[-1]


def sort_stack(s: Stack) -> Stack:
    stack_temp = Stack()
    while s:
        temp = s.pop()
        while stack_temp and stack_temp.peek() > temp:
            s.push(stack_temp.pop())
        stack_temp.push(temp)

    while stack_temp:
        s.push(stack_temp.pop())

    return s


if __name__ == '__main__':
    s = Stack()
    seq = ['2', '5', '1', '3', '1']

    for item in seq:
        s.push(item)

    s = sort_stack(s)
    print("The popped elements in sorted order: ")
    s.print_stack()