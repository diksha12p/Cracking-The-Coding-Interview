import unittest

def string_compression(s1 : str):

    result, count = [], 0
    for i in range(len(s1)):
        # Including i != 0 to avoid s1[-1] and s[0] comparison
        if i != 0 and s1[i] != s1[i-1]:
            result.append(s1[i-1])
            result.append(str(count))
            count = 0
        count += 1

    # Appending the last repeated char
    result.append(s1[-1])
    result.append(str(count))

    # return min(s1, "".join(result), key = len)
    return result


# class Test(unittest.TestCase):
#     data = [
#         ('aabcccccaaa', 'a2b1c5a3'),
#         ('abcdef', 'abcdef')
#     ]
#
#     def test_string_compression(self):
#         for [test_s1, expectation] in self.data:
#             actual = string_compression(test_s1)
#             self.assertEqual(actual, expectation)
#
#
# if __name__ == "__main__":
#     unittest.main()



s = ["a","a","b","b","c","c","c"]
s1 = "abcdeff"
print(string_compression(s))

