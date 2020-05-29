class Solution:
    def rotateString(self, str1: str, str2: str) -> bool:
        if str2 in str1+str1:
            return True
        else:
            return False


sol = Solution()
s1 = "bbbacddceeb"
s2 = "ceebbbbacdd"
print(sol.rotateString(s1,s2))