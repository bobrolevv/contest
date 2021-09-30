def bin_search(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    # elif x < arr[mid]:
    elif ((arr[mid] < arr[left] <= x)
        or (arr[left] <= x < arr[mid])
        or (x < arr[mid] < arr[left])):
        return bin_search(arr, x, left, mid)
    else:
        return bin_search(arr, x, mid + 1, right)




def broken_search(nums, target) -> int:
    # ==== TL 14 ====
    # for i in range(0, len(nums)):
    #     if target == nums[i]: return i
    # return -1
    # ==== TL 14 ====

    # nums1 = sorted(nums)
    # for delta in range(0, len(nums)):
    #     if nums1[0] == nums[delta]:
    #         break
    #     elif target == nums[delta]:
    #         return delta

    # n_target = bin_search(nums1, target, 0, len(nums1))
    n_target = bin_search(nums, target, 0, len(nums))
    return n_target# + delta if n_target != -1 else n_target

def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    # arr = [3, 5, 6, 7, 9, 1, 2]
    assert broken_search(arr, 5) == 6
    # print(broken_search(arr, 5))# == 6
# test()
