# id 0
# def member_tag(member, key):
#     return member[key]

def partition(array, pivot, key):
    less = []
    center = []
    greater = []
    for i in array:
        if i[key] < pivot: less.append(i)
        elif i[key] > pivot: greater.append(i)
        else: center.append(i)
    return less, center, greater

def quick_sort(array, key):
    '''
    key: 0-login, 1-штраф, 2-баллы
    02.10.2021 доделать:
    1. штраф, баллы -> int
    2. добавить in-place
    '''
    if len(array) < 2:
        return array
    else:
        pivot = array[0][key]
        less, center, greater = partition(array, pivot, key)
        return quick_sort(less, key) + center + quick_sort(greater, key)

if __name__ == '__main__':
    n = int(input())
    members = []
    for i in range(0, n):
        member = input().split()
        members.append(member)

    res = quick_sort(members, 2)
    print(*res, sep='\n')

