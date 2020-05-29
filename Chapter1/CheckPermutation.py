from collections import Counter


def check_permutation(s1, s2):
    dict_s1 = Counter(s1)
    k = len(s1)
    # Generate substrings of s2 such that the len(s2)== len(s1)
    for i in range(len(s2)):
        substr_s2 = s2[i:i+k]
        dict_sub_str_s2 = Counter(substr_s2)

        if dict_s1 == dict_sub_str_s2:
        # if sorted(s1) == sorted(substr_s2):
            return True
    return False


def rolling_hm(str1, str2):
    k = len(str1)
    d1 = Counter(str1)
    d2 = Counter(str2[:k])
    for i in range(len(str2) - k):
        if d2[str2[i]] == 1:
            del d2[str2[i]]
        elif d2[str2[i]] > 1:
            d2[str2[i]] -= 1

        if str2[i + k] in d2:
            d2[str2[i]] += 1
        else:
            d2[str2[i+k]] = 1

        if d1 == d2:
            return True
    return False


str1 = "abd"
str2 = "eidbaooo"
print(check_permutation(str1, str2))
print(rolling_hm(str1, str2))
