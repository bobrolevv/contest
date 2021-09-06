# Ближайший ноль ======================
import time
start_time = time.time()

street = input()
hoom = list(map(int, input().split()))
l = len(hoom)
res = [l]*l
i = 1
flag = False

for x in range(0, l):
    if hoom[x] == 0:
        i = 0
        flag = True

    if flag: res[x] = i
    i += 1

for y in range(l-1, -1, -1):
    if hoom[y] == 0:
        i = 0
    if res[y] > i: res[y] = i
    i += 1

print(" ".join(map(str, res)))

print("--- %s seconds ---" % (time.time() - start_time))
