# id 53206892
class DequeException(Exception):
    pass


class EmptyDeque(DequeException):
    pass


class FullDeque(DequeException):
    pass


class Deque:
    def __init__(self, n):
        self.items: list[any] = [None] * n
        self.maximum: int = n
        self.head: int = 0
        self.tail: int = 0
        self.size: int = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def push_back(self, item) -> list:
        if self.size != self.maximum:
            self.tail = (self.tail - 1) % self.maximum
            self.items[self.tail] = item
            self.size += 1
        else:
            raise FullDeque('stack is full')
            # print('error')

    def push_front(self, x) -> list:
        if self.size != self.maximum:
            self.items[self.head] = x
            self.head = (self.head + 1) % self.maximum
            self.size += 1
        else:
            raise FullDeque('stack is full')
            # print('error')

    def pop_front(self) -> object:
        if self.is_empty():
            raise EmptyDeque('stack is empty')
            # return 'error'
        # x = self.items[self.head - 1
        # self.items[self.head - 1] = None
        # self.head = (self.head - 1) % self.maximum
        self.head = (self.head - 1) % self.maximum
        x = self.items[self.head]
        # self.items[self.head - 1] = None

        self.size -= 1
        return x

    def pop_back(self) -> object:
        if self.is_empty():
            raise EmptyDeque('stack is empty')
        x = self.items[self.tail]
        self.items[self.tail] = None
        self.tail = (self.tail + 1) % self.maximum
        self.size -= 1
        return x

def deque_maker(input_data:str) -> list:
    result = []
    # использую чтение из файла, т.к. с input() не проходит TL 23 тесте
    with open(input_data) as input_data:
        command_count: int = int(input_data.readline())
        deque: Deque = Deque(int(input_data.readline()))

        for i in range(0, command_count):
            comm_list = input_data.readline().split()
            try:
                if comm_list[0] == 'push_back': deque.push_back(comm_list[1])
                elif comm_list[0] == 'pop_back': print(deque.pop_back())
                elif comm_list[0] == 'push_front': deque.push_front(comm_list[1])
                elif comm_list[0] == 'pop_front': print(deque.pop_front())
            except EmptyDeque:
                print('error')
            except FullDeque:
                pass

    return result

if __name__ == '__main__':

    input_data = 'input_A.txt'
    deque_maker(input_data)
