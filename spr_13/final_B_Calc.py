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
                 stack=Stack(),
                 methods=METHODS,
                 digit_maker=int):

    # Тут серьезная неочевидная ошибка новичков.Посмотрите на умолчательное
    # значение для параметра stack. Вы, скорее всего, не ожидаете, что это
    # значение будет вычисленно только один раз при первом вызове.
    # Более ожидаемое поведение - "вычисление при каждом вызове" - не
    # происходит. Есть готовый шаблон, для такой ситуации
    # def fun(data=None):
    #     data = calcucate_data() if data is None else data

    # Дико извиняюсь, что опять здесь пишу, но в слаке долго обяснять откуда
    # я это беру и о чем речь.
    # Здесь вообще ничего не понял, т.к. параметр stack я добавил по
    # рекомендации из предыдущего ревью. Соответственно и ожиданий по поводу
    # того, как он себя там поведет - нет.

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
