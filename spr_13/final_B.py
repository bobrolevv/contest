# id 53326152
import operator

METHODS = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           '/': operator.floordiv
           }


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items == []:
            raise ValueError('Stack is empty')
        else:
            return self.items.pop()


def polland_calc(input_file: str,
                 stack=Stack(),
                 methods=METHODS,
                 digit_maker=int) -> int:

    with open(input_file) as file:
        input_data = file.readline().split()

        for item in input_data:
            if item in methods:
                b = stack.pop()
                a = stack.pop()
                stack.push(methods[item](a, b))
            else: stack.push(digit_maker(item))

    return stack.pop()

if __name__ == '__main__':

    input_file = 'input.txt'
    result = polland_calc(input_file)
    print(result)

