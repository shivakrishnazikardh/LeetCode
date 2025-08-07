# Last updated: 8/6/2025, 10:03:35 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash = {}
        l, r = 0, 0
        charl = [0] * 26
        maxl, t = 0, 0

        for i in range(len(s)):
            hash[s[r]] = hash.get(s[r], 0) + 1
            lenl = r - l + 1

            if lenl - max(hash.values()) > k :
                hash[s[l]] -= 1
                l += 1
                t = 0
            
            else :
                t += 1
                maxl = max(maxl, lenl)
                
            
            r += 1

        return maxl





            
        