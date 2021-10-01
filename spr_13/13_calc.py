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
                 digit_maker=int):
    stack = Stack() if stack is None else stack

    for item in input_data:
        if item in methods:
            argument_2 = stack.pop()
            argument_1 = stack.pop()
            stack.push(methods[item](argument_1, argument_2))
        else:
            try:
                stack.push(digit_maker(item))
            except ValueError:
                raise ValueError(f'invalid literal {item}')

    return stack.pop()

if __name__ == '__main__':

    # input_data = input().split()
    print(polland_calc(input().split()))
