# палиндром ==========================================
# s = input()
# s = (s.translate({ord(i): None for i in ' ,:.'}).lower())
# if s == (s[::-1]):
#     print(True)
# else:
#     print(False)

# работа из дома ======================================
# d = int(input())
# res = d
# stroka = ""
# # print(len(d))
# while res != 1:
#     if res % 2:
#         stroka = (stroka + "1")
#     else:
#         stroka = (stroka + "0")
#
#     res = res // 2
# print(stroka)

# H/двоичная систенема ===================
# a = str(input())
# b = str(input())
# um = '0'
# summa = ''
# len_max = max(len(a), len(b))
# while len(a) != len(b):
#     if len(a) > len(b):
#         b = '0' + b
#     elif len(b) > len(a):
#         a = '0' + a
#
# for i in range(1, len_max+1):
#     if a[-i] == '1' and b[-i] == '1' and um == '0':
#         summa = summa + '0'
#         um = '1'
#     elif a[-i] == '1' and b[-i] == '1' and um == '1':
#         summa = summa + '1'
#         # um = '1'
#     elif a[-i] == '1' and b[-i] == '0' and um == '1':
#         summa = summa + '0'
#         # um = '0'
#         # um = '1'
#     elif a[-i] == '0' and b[-i] == '1' and um == '1':
#         summa = summa + '0'
#         # um = '0'
#         # um = '1'
#     elif a[-i] == '0' and b[-i] == '0' and um == '1':
#         summa = summa + '1'
#         um = '0'
#     elif a[-i] == '1' and b[-i] == '0' and um == '0':
#         summa = summa + '1'
#     elif a[-i] == '0' and b[-i] == '1' and um == '0':
#         summa = summa + '1'
#     elif a[-i] == '0' and b[-i] == '0' and um == '0':
#         summa = summa + '0'
# if um == '1':
#     summa = summa + '1'
# print(summa[::-1])

# I/ Степень четырех =============================
# import math
# a = int(input())
# b = math.log(a, 4)
# if (b % 1) == 0:
#     print('True')
# else:
#     print('False')

# J/ Факторизация числа =========================== TL ==
# def factor(a):
#     result = ''
#     lya = (lambda x, y: x // y)
#     while a != 1:
#         for i in range(2, a+1):
#             if a % i == 0:
#                 result = (f'{result}{str(i)} ')
#                 a = lya(a, i)
#                 break
#     return result
# print(factor(int(input())))

# s = input()
# t = input()
# l = len(t)
# for i in range(0, l):
#     if t[i] not in s:
#         print(t[i])
#         # break

# Ближайший ноль ======================
import traceback
def find_null(input_list, start):
    i1 = 0
    # i2 = 0
    res1 = None
    res2 = None
    for x in range(start, len(input_list)):
        if input_list[x] == 0:
            res1 = i1
            break
        i1 += 1

    i1 = 0
    for y in range(start, -1, -1):
        if input_list[y] == 0:
            res2 = i1
            break
        i1 += 1

    try:
        return min(res1, res2)
    except:
        if res1 is None: return res2
        if res2 is None: return res1

street = input()
hoom = list(map(int, input().split()))

l = ''
for x in range(0, len(hoom)):
    l = l + str(find_null(hoom, x)) + ' '

print(list(map)
