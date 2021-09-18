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
            self.item[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
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
            return None
        x = self.deque[self.head]
        self.deque[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def pop_back(self):
        pass

    def __str__(self):
        return '-'.join(str(x) for x in self.item)

comand_count = int(input())
max_leght = int(input())
deque = Deque(max_leght)

# result_list = ['====',]

# command_list = []

# while comand_count:
#     command_list = input().split()
#     print(command_list)
#     result_push = []
#
#     if 'push_back' in command_list:
#         result_push = deque.push_back(command_list[1])
#         if result_push == 'error':
#             result_list.append(result_push)
#
#     if 'pop_back' in command_list:
#         result_list.append(deque.pop_back())
#
#     if 'push_front' in command_list:
#         print('pfr')
#         result_push = deque.push_front(command_list[1])
#         print(result_push)
#         if result_push == 'error':
#             result_list.append(result_push)
#             print(result_list)
#
#     if 'pop_front' in command_list:
#         result_list.append(deque.pop_front())
#
#     comand_count -= 1

# if __name__ == '__main__':
#     for i in result_list:
#         print(i)

deque.push_front(1111)
print(deque.head, deque, deque.tail, deque.size)
deque.push_front(2222)
print(deque.head, deque, deque.tail, deque.size)
deque.push_front(3333)
print(deque.head, deque, deque.tail, deque.size)
deque.push_front(7777)
print(deque.head, deque, deque.tail, deque.size)
