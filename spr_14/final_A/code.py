def broken_search(nums, target) -> int:
    # nums.sort()

    # for i in range(0, len(nums)):
        # print(i, nums[i])
    i = len(nums)-1
    if target == nums[i]:
        return i
    else:
        nums.pop()
        print(nums, len(nums))
        broken_search(nums, target)
        # return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    # assert broken_search(arr, 5) == 6
    print(broken_search(arr, 5))# == 6
test()