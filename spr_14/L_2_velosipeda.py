# 00000
if __name__ == '__main__':
    days: int = int(input())
    data: list = input().split()
    price: int = int(input())

    result = [-1, -1]
    bike_index = 0
    for day_index in range(0, days - 1):
        if int(data[day_index]) >= price and bike_index <= 1:
            result[bike_index] = (day_index + 1)
            price = price * 2
            bike_index += 1

    print(*result, sep=' ')
