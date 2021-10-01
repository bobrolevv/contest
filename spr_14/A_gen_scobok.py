def gen(n: int, counter_open: int, counter_close: int, ans: str):
    if counter_open + counter_close == 2 * n:
        print(ans)
        return
    if counter_open < n:
        gen(n, counter_open + 1, counter_close, ans + '(')
    if counter_open > counter_close:
        gen(n, counter_open, counter_close + 1, ans + ')')

n = int(input())
gen(n, 0, 0, "")

# prefix = '()'
#
# def generator(n, prefix):
#     if i == 0:
#         print(prefix)
#     else:
#         generator(n, )
#     i = n-1
#     print('('*(i) + '()'*(n-i) + (i)*')')
#     i = n-2
#     print('('*(i) + '()'*(n-i) + (i)*')')
#     i = n-3
#     print('('*(i) + '()'*(n-i) + (i)*')')
#
#
# generator(3, prefix)

#     if n == 0:
#         print(prefix)
#     else:
#         generator(n - 1, prefix * n)
#         generator(n - 1, '('*n + prefix + ')'*n)
# n=3
# print(generator(n, prefix))