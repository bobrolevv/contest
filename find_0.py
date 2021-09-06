# Ближайший ноль ======================
# import traceback
import time
start_time = time.time()

def find_null(input_list, start):
    i1 = 0
    res1 = 0
    # res1 = None
    # res2 = None
    len_list = len(input_list)
    for x in range(start, len_list):
        if input_list[x] == 0:
            res1 = i1
            break
        i1 += 1

    i1 = 0
    for y in range(start, -1, -1):
        if input_list[y] == 0:
            if i1 <= res1: res1 = i1
            # res2 = i1
            break
        i1 += 1

    return res1
    # try:
    #     return min(res1, res2)
    # except:
    #     if res1 is None: return res2
    #     if res2 is None: return res1

street = input()
hoom = list(map(int, input().split()))

# l = len(hoom)
# data = [0] * l
# for i in range(l):
#     data[i] = str(find_null(hoom, i))
# print(" ".join(data))
print(" ".join([str(find_null(hoom, x)) for x in range(0, len(hoom))]))

print("--- %s seconds ---" % (time.time() - start_time))