a = [[4,7,2,8,5], [5,6,6,8,9]]

for i in range(len(a)):
    # print(range(len(a)))
    for j in range(len(a[i])):
        print(range(len(a[i])))
        if a[i][j]%2 == 0:
            a[i][j]=0


print(a)