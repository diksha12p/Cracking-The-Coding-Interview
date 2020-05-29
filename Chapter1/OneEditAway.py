class Solution:
    def one_edit_away(self,s1,s2):
        if len(s1) == len(s2):
            return self._one_edit_replace(s1,s2)
        elif len(s1) + 1 == len(s2):
            return self._one_edit_insert(s1,s2)
        elif len(s1) - 1 == len(s2):
            return self._one_edit_insert(s2,s1)
        return False

    def _one_edit_replace(self,s1,s2):
        flag = False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if flag: return False
                flag = True
        return True

    def _one_edit_insert(self,s1,s2):
        flag, i, j = False, 0, 0
        while i < len(s1) and j < len(s2):
            if s1[i] != s2[j]:
                if flag: return False
                flag = True
                j += 1
            else:
                i += 1
                j += 1
        return True


sol = Solution()
s1, s2 = 'pale', 'pse'
print(sol.one_edit_away(s1,s2))



