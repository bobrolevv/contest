n1 = int(input())
# data = sorted(list(map(int, input().split())))
data = input().split()
# print(data)
ans = []
def combi(data: list, counter: int, n: int, ans: list):
    if counter == n1:
        print(ans)#, end=' ')
        return
    if counter < n1:
        for i in data:
            ans.append(i)
            combi(data, counter + 1, n + 1, ans)

combi(data, 0, 0, [])