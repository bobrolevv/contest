prefix = '()'

def generator(n, prefix):
    if i == 0:
        print(prefix)
    else:
        generator(n, )
    i = n-1
    print('('*(i) + '()'*(n-i) + (i)*')')
    i = n-2
    print('('*(i) + '()'*(n-i) + (i)*')')
    i = n-3
    print('('*(i) + '()'*(n-i) + (i)*')')


generator(3, prefix)




#     if n == 0:
#         print(prefix)
#     else:
#         generator(n - 1, prefix * n)
#         generator(n - 1, '('*n + prefix + ')'*n)
# n=3
# print(generator(n, prefix))