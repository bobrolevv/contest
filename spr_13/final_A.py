class Deque:
    def __init__(self, n) -> object:
        self.item = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, x):
        if self.size != self.max_n:
            self.item[self.head] = x
            self.tail = (self.head + 1) % self.max_n
            self.size += 1
        else:
            return 'error'

    def push_front(self, x):
        if self.size != self.max_n:
            self.item[self.head] = x
            self.head = (self.head + 1) % self.max_n
            self.size += 1
        else:
            return 'error'

    def pop_front(self):
        if self.is_empty():
            return 'error'
        x = self.item[self.head -1]
        self.item[self.head - 1] = None

        self.head = (self.head - 1) % self.size
        self.size -= 1
        return x

    def pop_back(self):
        if self.is_empty():
            return 'error'
        x = self.item[self.tail - 1]
        self.item[self.tail - 1] = None

        self.tail = (self.tail - 1) % self.size
        self.size -= 1
        return x

    def __str__(self):
        return '-'.join(str(x) for x in self.item)



def test():
    comand_count = int(input())
    max_leght = int(input())
    deque = Deque(max_leght)

    while comand_count:
        command_list = input().split()
        if 'push_back' in command_list:
            res = deque.push_back(command_list[1])
            print(deque.item[0])
            if res: print(res)

        if 'pop_back' in command_list:
            res = deque.pop_back()
            if res: print(res)

        if 'push_front' in command_list:
            res = deque.push_front(command_list[1])
            print(deque.item)
            if res: print(res)

        if 'pop_front' in command_list:
            res = deque.pop_front()
            if res: print(res)

        comand_count -= 1

if __name__ == '__main__':
    test()