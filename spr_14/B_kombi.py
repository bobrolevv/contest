NO_KIA = {
    2:'abc',
    3:'def',
    4:'ghi',
    5:'jkl',
    6:'mno',
    7:'pqrs',
    8:'tuv',
    9:'wxyz'
}


def combi(data: list, counter: int, n:int, ans: list):
    if counter == len(data):
        print(ans, end=' ')
        return
    if counter < len(data):
        for i in data[n]:
            combi(data, counter + 1, n+1, ans + i)

inp = input()
data = []
for i in range(0, len(inp)):
    d = int(inp[i])
    data.append(NO_KIA[d])

combi(data, 0, 0, '')
