from typing import List


class Deque:
    def __init__(self, n) -> object:
        self.item = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self) -> object:
        return self.size == 0

    def push_back(self, x):
        if self.size != self.max_n:
            self.item[self.tail -1] = x
            self.tail = (self.tail - 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def push_front(self, x):
        if self.size != self.max_n:
            self.item[self.head] = x
            self.head = (self.head + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop_front(self):
        if self.is_empty():
            return 'error'
        x = self.item[self.head - 1]
        self.item[self.head - 1] = None
        self.head = (self.head - 1) % self.max_n
        self.size -= 1
        return x

    def pop_back(self):
        if self.is_empty():
            return 'error'
        x = self.item[self.tail]
        self.item[self.tail] = None
        self.tail = (self.tail + 1) % self.max_n
        self.size -= 1
        return x

    # def __str__(self):
    #     return '-'.join(str(x) for x in self.item)



def test() -> object:
    comand_count: int = int(input())
    max_leght: int = int(input())
    deque: Deque = Deque(max_leght)

    while comand_count:
        command_list: List[str] = input().split()

        if 'push_back' in command_list:
            deque.push_back(command_list[1])

        elif 'pop_back' in command_list:
            print(deque.pop_back())

        elif 'push_front' in command_list:
            deque.push_front(command_list[1])

        elif 'pop_front' in command_list:
            print(deque.pop_front())
            
        comand_count -= 1

if __name__ == '__main__':
    test()
