# id 53737960

def partition(array, pivot):
    less = []
    center = []
    greater = []
    for elem in array:
        if elem < pivot:
            less.append(elem)
        elif elem > pivot:
            greater.append(elem)
        else:
            center.append(elem)
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
    for _ in range(0, n):
        member = input().split()
        member[1] = -int(member[1])
        member[2] = int(member[2])
        members.append([member[1], member[2], member[0]])

    res = quick_sort(members)

    print("\n".join([name[2] for name in res]))
