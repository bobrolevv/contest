class Deque:
    def __init__(self, n) -> object:
        self.deque = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1

    def push_front(self, x):
        pass

    def pop_front(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def pop_back(self):
        pass

comand_count = int(input())
max_leght = int(input())
deque = Deque(max_leght)
result_list = []

while comand_count:
    command_list = input().split()
    result_push = []

    if 'push_back' in command_list:
        result_push = deque.push_back(command_list[1])
        if result_push == 'error':
            result_list.append(result_push)

    if 'pop_back' in command_list:
        result_list.append(deque.pop_back())

    if 'push_front' in command_list:
        result_push = deque.push_front(command_list[1])
        if result_push == 'error':
            result_list.append(result_push)

    if 'pop_front' in command_list:
        result_list.append(deque.pop_front())

    comand_count -= 1

if __name__ == '__main__':
    for i in result_list:
        print(i)
