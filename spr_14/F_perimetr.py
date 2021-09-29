n = int(input())
# lenghts = list(map(int, input().split()))
# lenghts = sorted(lenghts, reverse=True)
lenghts = sorted(list(map(int, input().split())), reverse=True)

for i in range(0, len(lenghts)):
    c = lenghts[i]
    a = lenghts[i+1]
    b = lenghts[i+2]
    if c < a + b:
        res = a+b+c
        break
print(res)
