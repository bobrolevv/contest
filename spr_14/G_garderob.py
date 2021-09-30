n = int(input())
vuzs = sorted(list(map(int, input().split())))
# print(vuzs)
print(*vuzs, sep=' ')