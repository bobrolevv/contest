n = int(input())
klumbs = []

while n != 0:
    k = list(map(int, input().split()))
    klumbs.append(k)
    n -= 1

klumbs.sort()

res = []
res.append(klumbs[0])

for i in range(0, len(klumbs) - 1):
    l = len(res)
    if klumbs[i + 1][0] > res[l-1][1]:
        res.append(klumbs[i + 1])
    else:
        if klumbs[i + 1][1] > res[l-1][1]:
            res[l - 1][1] = klumbs[i + 1][1]

for i in res:
    print(i[0], i[1])
