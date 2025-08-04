# Last updated: 8/4/2025, 4:57:53 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = set()
        l, r = 0, 0
        msub= 0

        for i in range(len(s)):
            while s[r] in hash :
                hash.remove(s[l])
                l += 1
                                
            
            hash.add(s[r])
            r += 1
            msub = max(r-l, msub)
                
        return msub
                

