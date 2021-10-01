# id 0
def member_tag(member, key):
    return member[key]

def partition(array, pivot):
    less = []
    center = []
    greater = []
    for i in array:
        if i < pivot: less.append(i)
        elif i > pivot: greater.append(i)
        else: center.append(i)
    return less, center, greater

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less, center, greater = partition(array, pivot)
        return quick_sort(less) + center + quick_sort(greater)

if __name__ == '__main__':
    n = int(input())
    members = []
    for i in range(0, n):
        member = input().split()
        members.append(member)




    # for i in range(0, len(members)):
    # print(*members, sep='\n')

    # print(partition([1, 13, 5, 8, 5, 56, 18], 13))
    # print(quick_sort([1, 13, 5, 8, 5, 56, 18]))
