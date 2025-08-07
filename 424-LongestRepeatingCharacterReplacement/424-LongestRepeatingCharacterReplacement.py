# Last updated: 8/6/2025, 10:56:26 PM
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
        