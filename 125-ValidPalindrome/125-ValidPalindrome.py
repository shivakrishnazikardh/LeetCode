# Last updated: 7/30/2025, 2:04:09 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''l, r = 0, len(s)-1

        while l < r :
            if l < r and not self.alphaNum(s[l]):
                l+=1
                continue
            if l < r and not self.alphaNum(s[r]):
                r-=1
                continue
            
            if s[l].lower() != s[r].lower():
                return False

            l,r = l+1, r-1

        return True

    def alphaNum(self, s):
        return (ord('A') <= ord(s) <= ord('Z') or ord('a') <= ord(s) <= ord('z') or ord('0') <= ord(s) <= ord('9')) '''

        new = ""
        for i in s:
            if i.isalnum() :
                new += i.lower()
        return new == new[::-1]
