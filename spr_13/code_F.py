class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items == []:
            print('error')
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def get_max(self):
        if self.items == []:
            return 'None'
        return max(self.items)


stack = Stack()
# stack.push(1)
# stack.push(3)
# stack.push(555)
# stack.push(7)

n = int(input())
while n:
    com_list = input().split()
    # print(com_list)

    if 'push' in com_list: stack.push(int(com_list[1]))
    elif 'pop' in com_list: stack.pop()
    elif 'get_max' in com_list: print(stack.get_max())
    n -= 1

# print('вы ввели', stack.pop())
