def urlify(str1, n):
    str1 = list(str1)
    curr_index = len(str1)
    for i in range(n-1, -1,-1):
        if str1[i] == " ":
            str1[curr_index - 3: curr_index] = '%20'
            curr_index -= 3
        else:
            str1[curr_index - 1] = str1[i]
            curr_index -= 1
    return "".join(str1)


s = "Mr John Smith    "
print(urlify(s,13))
# print(len(s))
# print(s.rstrip().count(" "))
# list = [i for i in range(9, -1, -1)]
# print(list)
# print(*reversed(range(12)))
#

# range(n-1, -1,-1)