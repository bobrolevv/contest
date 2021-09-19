# id 53206892
class Deque:
    def __init__(self, n) -> object:
        self.item: list[str] = [None] * n
        self.max_n: int = n
        self.head: int = 0
        self.tail: int = 0
        self.size: int = 0

    def is_empty(self) -> object:
        return self.size == 0

    def push_back(self, x) -> object:
        if self.size != self.max_n:
            self.item[self.tail - 1] = x
            self.tail = (self.tail - 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def push_front(self, x) -> object:
        if self.size != self.max_n:
            self.item[self.head] = x
            self.head = (self.head + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop_front(self) -> object:
        if self.is_empty():
            return 'error'
        x = self.item[self.head - 1]
        self.item[self.head - 1] = None
        self.head = (self.head - 1) % self.max_n
        self.size -= 1
        return x

    def pop_back(self) -> object:
        if self.is_empty():
            return 'error'
        x = self.item[self.tail]
        self.item[self.tail] = None
        self.tail = (self.tail + 1) % self.max_n
        self.size -= 1
        return x

def test() -> object:
    with open('input.txt') as inpt:
        comand_count: int = int(inpt.readline())
        max_leght: int = int(inpt.readline())
        deque: Deque = Deque(max_leght)

        for i in range(0, comand_count):
            command_list = inpt.readline().split()
            if command_list[0] == 'push_back':
                deque.push_back(command_list[1])
            elif command_list[0] == 'pop_back':
                print(deque.pop_back())
            elif command_list[0] == 'push_front':
                deque.push_front(command_list[1])
            elif command_list[0] == 'pop_front':
                print(deque.pop_front())

if __name__ == '__main__':
    test()
