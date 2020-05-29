def transpose(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr[0])):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]


def flip_by_symmetry(mat):
    for j in range(len(mat[0]) // 2):
        for i in range(len(mat)):
            mat[i][j], mat[i][-(j + 1)] = mat[i][-(j + 1)], mat[i][j]


def rotate_by_90(arr):
    transpose(arr)
    flip_by_symmetry(arr)
