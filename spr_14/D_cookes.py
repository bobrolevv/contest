a = input()
b = list(map(int, input().split()))
c = input()
d = list(map(int, input().split()))
print(a, b, c, d, sep='\n')
res = []
for i in b:
    for k in range(0, len(d)):
        if i <= d[k]:
            res.append(d[k])
            print(d, d[k])
            d.pop(k)
            break
print(res, len(res))
# print(len(res))

