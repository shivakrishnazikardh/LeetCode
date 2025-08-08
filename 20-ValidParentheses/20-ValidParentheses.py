# Last updated: 8/7/2025, 11:01:07 PM
class Solution:
    def isValid(self, s: str) -> bool:
        hash = []
        countermap = {')':'(', ']':'[', '}':'{'}

        for i in s :
            if i in countermap :
                if hash and hash[-1] == countermap[i] :
                    hash.pop()
                else :
                    return False
            else :
                hash.append(i)

        return True if not hash else False
        