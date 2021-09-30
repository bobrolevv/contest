# id 53688085
def bin_search(nums, tgt, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if nums[mid] == tgt:
        return mid
    elif ((nums[mid] < nums[left] <= tgt)
          or (nums[left] <= tgt < nums[mid])
          or (tgt < nums[mid] < nums[left])):
        return bin_search(nums, tgt, left, mid)
    else:
        return bin_search(nums, tgt, mid + 1, right)

def broken_search(nums, target) -> int:
    return bin_search(nums, target, 0, len(nums))

def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
    # print(broken_search(arr, 5))# == 6
# test()
