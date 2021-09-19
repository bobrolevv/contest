class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items == []:
            print('error')
        else:
            return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def get_max(self):
        if self.items != []:
            return max(self.items)
        return 'None'

    def __str__(self):
        return '-'.join(str(x) for x in self.items)

def sum(a, b: int) -> int:
    return (a + b)

def razn(a, b: int) -> int:
    return (b - a)

def proizv(a, b: int) -> int:
    return (a * b)

def delen(a, b: int) -> int:
    return (b // a)

def test() -> int:
    method_dict = {'+': sum,
                   '-': razn,
                   '*': proizv,
                   '/': delen}

    stack = Stack()
    with open('input.txt') as file:

        inpt = file.readline().split()

        for i in inpt:
            if i in method_dict:
                a = int(stack.pop())
                b = int(stack.pop())
                res = method_dict[i](a, b)
                stack.push(res)
            else: stack.push(i)

    print(stack.pop())

if __name__ == '__main__':
    test()
