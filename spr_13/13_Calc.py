# id 53416551
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

def polland_calc(input_data: list,
                 stack=None,
                 methods=METHODS,
                 digit_maker=None):
    stack = Stack() if stack is None else stack
    digit_maker = int if digit_maker is None else digit_maker

    for item in input_data:
        if item in methods:
            argument_1 = stack.pop()
            argument_2 = stack.pop()
            stack.push(methods[item](argument_2, argument_1))
        else:
            try:
                stack.push(digit_maker(item))
            except ValueError:
                raise ValueError('invalid literal, need digits')

    return stack.pop()

if __name__ == '__main__':

    input_data = input().split()
    print(polland_calc(input_data))
