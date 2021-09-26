DICT_1 = {
    2:'abc',
    3:'def',
    4:'ghi',
    5:'jkl',
    6:'mno',
    7:'pqrs',
    8:'tuv',
    9:'wxyz'
}
# нужны три параметра:
# набор кнопок, которые будем обрабатывать
# текущая строка букв
# массив с результатами

def combi(data: str,
          strg: str,
          counter: int,
          ans: str):

    if counter == len(data):
        return ans
    else:

        combi(data, strg, counter+1, ans + data[]):






# ===============
# def combi(data, prefix='', n=0, result=None):
#     result = [] if result is None else result
#     if len(prefix) == 2:
#         result.append(prefix)
#     else:
#         for i in data[n]:
#             combi(data, prefix+i, n+1, result)
#         combi(data, prefix, n+1, result)
#     return result
# # ===============
#
# # def combi(data: list,
# #           variants:list,
# #           counter: int,
# #           x: int,
# #           y: int,
# #           ans: str):
# #
# #     if counter == variants[0]:
# #         print(ans)
# #         return
# #     if counter < variants[0]:
# #         # n = len(data[0])
# #         combi(data,
# #               variants,
# #               counter + 1,
# #               # if x < 3: x+=1 else x=0,
# #               x-1 if x!=0 else variants[1],
# #               y-1 if y!=len(data[1]) else 0,
# #               ans + data[variants[1] - x][y-1] + ' '
# #         )
#
# inp = input()
# data = []
# variants = [1, 1]
# for i in range(0, len(inp)):
#     d = int(inp[i])
#     data.append(DICT_1[d])
#     variants[0] = variants[0] * len(DICT_1[d])
#
# variants[1] = len(data)
# # print(data, variants)
#
# # combi(data, variants, 0, variants[1], len(data[0]), '')
# combi(data)
