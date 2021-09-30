# 00000
import cProfile



def velo():
    days: int = int(input())
    data: list = list(map(int, input().split()))
    price: int = int(input())

    result = [-1, -1]
    bike_index = 0
    for day_index in range(0, days):
        if data[day_index] >= price and bike_index <= 1:
            result[bike_index] = (day_index + 1)
            price = price * 2
            bike_index += 1

    print(*result, sep=' ')

if __name__ == '__main__':

    # velo()
    cProfile.run('velo')

# # 00000
# def binarySearch(data, price, left, right):
#     if right <= left:
#         return -1
#
#     mid = (left + right) // 2
#
#     if int(data[mid]) // price == 1:  # центральный элемент — искомый
#         return mid
#     elif price < int(data[mid]):
#         return binarySearch(data, price, left, mid)
#     else:
#         return binarySearch(data, price, mid + 1, right)
#
# def minSearch(data, index):
#     if int(data[index-1]) < int(data[index]) or index == 0:
#         return index
#     elif index == - 1:
#         return index - 1
#     else:
#         return minSearch(data, index - 1)
#
# def main():
#     days: int = int(input())
#     data: list = input().split()
#     price: int = int(input())
#
#     index = binarySearch(data, price, 0, days - 1)
#     index2 = binarySearch(data, price*2, index, days - 1)
#
#     print(minSearch(data, index) + 1, minSearch(data, index2) + 1)
#
# if __name__ == '__main__':
#     main()
