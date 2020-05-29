def check_permutation_symetric(str1, str2):
    # Type of string? ASCII / Unicode? Assume, ASCII.
    # Thus, character set length = 128

    if len(str1) != len(str2):
        return False

    char_count = [0] * 128
    for char in str1:
        char_count[ord(char)] += 1

    for char in str2:
        char_count[ord(char)] -= 1
        if char_count[ord(char)] < 0:
            return False

    return True


s1 = "dog       "
s2 = "dog"
print(check_permutation_symetric(s1,s2))
print(s1.strip().upper())
# for char in s1:
#     print(ord(char))

