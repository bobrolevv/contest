'''
merge(arr: list, left: int, mid: int, right: int) -> array
merge_sort(arr: list, left: int, right: int) -> None
'''

def merge(arr, lf, mid, rg):

	left = merge_sort(arr[0:lf], 0, lf)
	right = merge_sort(arr[mid:rg], mid, rg)

	result = [] * len(arr)

	l, r, k = 0, 0, 0
	while l < len(left) and r < len(right):
		if left[l] <= right[r]:
			result[k] = left[l]
			l += 1
		else:
			result[k] = right[r]
			r += 1
		k += 1

		while l < len(left):
			result[k] = left[l]
			l += 1
		k += 1

		while r < len(right):
			result[k] = right[r]
			r += 1
	k += 1

	return result


def merge_sort(arr, lf, rg):
	arr.sort()
	# if len(arr) == 1:
	# return arr

def test():
	# a = [1, 4, 9, 2, 10, 11]
	# b = merge(a, 0, 3, 6)
	# expected = [1, 2, 4, 9, 10, 11]
	# assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	print(merge_sort(c, 0, 6))
	# expected = [1, 1, 2, 2, 4, 10]
	# assert c == expected

test()