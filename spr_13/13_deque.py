# id 53416665
class DequeException(Exception):
    pass


class Deque:
    def __init__(self, lenth):
        self.items: list = [None] * lenth
        self.maximum: int = lenth
        self.head: int = 0
        self.tail: int = 1
        self.size: int = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def push_back(self, item):
        if self.size == self.maximum:
            raise DequeException('stack is full')
        self.tail = (self.tail - 1) % self.maximum
        self.items[self.tail] = item
        self.size += 1

    def push_front(self, item):
        if self.size == self.maximum:
            raise DequeException('stack is full')
        self.head = (self.head + 1) % self.maximum
        self.items[self.head] = item
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise DequeException('stack is empty')
        item = self.items[self.head]
        self.head = (self.head - 1) % self.maximum
        self.size -= 1
        return item

    def pop_back(self):
        if self.is_empty():
            raise DequeException('stack is empty')
        item = self.items[self.tail]
        self.tail = (self.tail + 1) % self.maximum
        self.size -= 1
        return item

    def __str__(self):
        return '-'.join(str(x) for x in self.items)

if __name__ == '__main__':

    command_count: int = int(input())
    deque: Deque = Deque(int(input()))
    result = []

    for _ in range(0, command_count):
        item = None
        command, *params = input().split()
        try:
            item = getattr(deque, command)(*params)
        except DequeException:
            item = 'error'
        except AttributeError:
            raise ValueError(f'value for {command} is unexpected')

        if item != None: result.append(item)

    print(*result, sep='\n')
