# id 53404058
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
        try:
            return self.items.pop()
        except IndexError:
            return 'Stack is empty'

def polland_calc(input_data: str,
                 stack=None,
                 methods=METHODS,
                 digit_maker=int):
    stack = Stack() if stack is None else stack
    input_data = input_data.split()
    for item in input_data:
        if item in methods:
            argument_b = stack.pop()
            argument_a = stack.pop()
            stack.push(methods[item](argument_a, argument_b))
        else:
            try:
                digit = digit_maker(item)
            except ValueError:
                return 'invalid literal for digit_maker'
            stack.push(digit)

    return stack.pop()

if __name__ == '__main__':

    input_data = input()
    result = polland_calc(input_data)
    print(result)
