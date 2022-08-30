sum = 0

for line in range(991):
    sum += line

print(sum)

#  求最大数的 key
listarray = {"a":100, "b":444,"c":2}
# max(字典) , key =
print(max(listarray))

print(max(listarray, key=lambda value: listarray[value]))


