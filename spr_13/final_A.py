# id 53323246
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

    def push_front(self, item) -> list:
        if self.size != self.maximum:
            self.items[self.head] = item
            self.head = (self.head + 1) % self.maximum
            self.size += 1
        else:
            raise FullDeque('stack is full')

    def pop_front(self) -> list:
        if self.is_empty():
            raise EmptyDeque('stack is empty')

        self.head = (self.head - 1) % self.maximum
        item = self.items[self.head]

        self.size -= 1
        return item

    def pop_back(self) -> list:
        if self.is_empty():
            raise EmptyDeque('stack is empty')

        item = self.items[self.tail]
        self.tail = (self.tail + 1) % self.maximum
        self.size -= 1
        return item

    def __str__(self):
        return '-'.join(str(x) for x in self.items)

def deque_maker(input_data:str) -> list:
    result = []
    # использую чтение из файла, т.к. с input() не проходит TL 23 тесте
    with open(input_data) as input_data:
        command_count: int = int(input_data.readline())
        deque: Deque = Deque(int(input_data.readline()))

        for i in range(0, command_count):
            cmnd, *prms = input_data.readline().split()

            try:
                # getattr(deque, cmnd(*prms)) # - очень локанично, но у меня
                # вызывает ошибку: TypeError: 'str' object is not callable
                # --------------------
                # пробовал так:
                # getattr(deque, f'{cmnd}({*prm})')  # так на синтаксис руг-ся
                #                          ^
                # SyntaxError: can't use starred expression here

                if cmnd == 'push_back': deque.push_back(*prms)
                elif cmnd == 'pop_back': result.append(deque.pop_back())
                elif cmnd == 'push_front': deque.push_front(*prms)
                else: result.append(deque.pop_front())
            except EmptyDeque:
                result.append('error')
            except FullDeque:
                result.append('error')
    return result

if __name__ == '__main__':

    input_data = 'input.txt'
    result = deque_maker(input_data)
    for i in result:
        print(i)
