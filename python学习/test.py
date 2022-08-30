a=[
[1,2,8,9],
[2,4,9,12],
[4,7,10,13],
[6,8,11,15]
]



def getArrayIndex(a):
    i = 0
    j = len(a[0]) - 1
    target = 11
    while i< len(a) and j >=0 :
        if a[i][j]< target:
            i+=1
        elif a[i][j]> target:
            j-=1
        else:
            return i ,j
    return False

print(getArrayIndex(a))


for i , j in enumerate(a):
    print(i,j)