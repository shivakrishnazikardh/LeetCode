# Last updated: 8/5/2025, 10:43:56 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash = []
        l, r = 0, 0
        charl = [0] * 26
        maxl, t = 0, 0

        for i in range(len(s)):
            charl[ord(s[r]) - ord('A')] += 1
            lenl = r - l + 1

            if lenl - max(charl) > k :
                charl[ord(s[l]) - ord('A')] -= 1
                l += 1
                t = 0
            
            else :
                t += 1
                maxl = max(maxl, lenl)
                hash.append(maxl)
            
            r += 1

        return maxl





            
        