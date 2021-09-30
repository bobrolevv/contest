arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
arr.sort()
print(arr)
b = len(arr)
# print(b)

def bin_search(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    elif x < arr[mid]:
        return bin_search(arr, x, left, mid)
    else:
        return bin_search(arr, x, mid + 1, right)

print(bin_search(arr, 5, 0, b)+4)
