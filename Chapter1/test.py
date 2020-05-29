mat = [[1,2,3],
  [4,5,6],
  [7,8,9]]

mat = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
for j in range(len(mat[0]) // 2):
    for i in range(len(mat)):
        # print("OLD: {} and {}".format(mat[i][j], mat[i][~j]))
        mat[i][j], mat[i][-(j+1)] = mat[i][-(j+1)], mat[i][j]
        # print("NEW : {} and {}".format(mat[i][~j], mat[i][j]))

# for i in range(len(mat[0])):
#     for j in range(len(mat)):
#         print(mat[i][j], end = " ")
#     print("\n")
# print(mat)


str1 = "waterbottle"
str2 = "erbottlewat"

# find first occurrence of str1[0] in str2 -> Pivot
pivot = str2.index(str1[0])
print(pivot)
x, y = str2[pivot:], str2[:pivot]
print(x,y)

if x+y == str1:
    print(True)
else:
    print(False)

