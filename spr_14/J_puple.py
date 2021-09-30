n = int(input())
data = list(map(int, input().split()))
# print(n, data, '\n', '-'*10)
temp = 0
b = 1
x = True
for k in range(0, n-1):
    count = 0
    for i in range(0, n-b):
        if data[i] > data[i+1]:
            temp = data[i+1]
            data[i + 1] = data[i]
            data[i] = temp
            count += 1
            x=False
    b += 1
    if count == 0:
        # print(*data, sep=' ')
        break
    else:
        print(*data, sep=' ')

if x:
    print(*data, sep=' ')
