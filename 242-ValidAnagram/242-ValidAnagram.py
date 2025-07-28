# Last updated: 7/28/2025, 12:51:26 PM
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

        if len(s) != len(t) :
            return False
        d1,  d2 = {}, {}
        for i in range(len(s)) :
            d1[s[i]] = 1 + d1.get(s[i], 0)
            d2[t[i]] = 1 + d2.get(t[i], 0)
        for j in d1:
            if d1[j] != d2.get(j, 0) :
                return False
        else:
            return True

        