# def getArraySum(array):
#     j = 0
#     # 3 1 2 4
#     newArray = []
#     while j < len(array) - 1:
#         tempArray = array[j:]
#         for k, _ in enumerate(tempArray):
#             i = 0
#             while i <= len(tempArray):
#                 if i == len(tempArray) and k == 1:
#                     i += 1
#                     continue
#                 if i > k:
#                     newArray.append(tempArray[k:i])
#                 i += 1
#         j += 1
#     return newArray
#
# # [[3], [3, 1], [3, 1, 2], [3, 1, 2, 4], [1], [1, 2], [1, 2, 4], [2], [2, 4], [4], [1], [1, 2], [1, 2, 4], [2], [2, 4], [4], [2], [2, 4], [4]]
# #
# sum = getArraySum([3, 1, 2, 4])
# print(sum)
a = [1, 2, 3, 4]
# b = a[1:4]
# print([0]*len(a))
# print(min(a))
# a=[0]
# print(a[-1])
# # b = a[1:4]
# c = a[4:]
# print(b)
# print(c)

for line in range(len(a)):
    print(line)
