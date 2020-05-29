from collections import Counter


# Using inbuilt Counter() method
def palindrome_permutation(s):
    d = Counter(s.lower().replace(" ",""))
    count = 0

    for value in d.values():
        if value % 2: count += 1
    return count <= 1


# Without using inbuilt Counter() method
# Without using lower() and replace() methods
def char_number(c):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    val = ord(c)

    if a <= val <= z:
        return val - a
    elif A <= val <= Z:
        return val - A
    return -1


def alt_palindrome_permutation(s):
    data_log = [0 for _ in range(ord('a'), ord('z') + 1)]
    count = 0
    for char in s:
        char_val = char_number(char)

        if char_val != -1:
            data_log[char_val] += 1

            if data_log[char_val] % 2:
                count += 1
            else:
                count -= 1
    return count <= 1


s = "Tact Coa"
print(palindrome_permutation(s))

print(alt_palindrome_permutation(s))