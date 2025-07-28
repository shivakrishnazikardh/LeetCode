# Last updated: 7/28/2025, 12:51:31 PM
class Solution(object):
    def groupAnagrams(self, strs):
        group = defaultdict(list)

        for i in strs :
            countaz = [0] * 26

            for j in i :
                countaz[ord(j)-ord('a')]+= 1

            group[tuple(countaz)].append(i)

        return group.values()
        