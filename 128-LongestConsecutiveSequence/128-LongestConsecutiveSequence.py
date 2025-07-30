# Last updated: 7/29/2025, 10:28:44 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set(nums)
        longest = 0

        for n in hash :
            if (n-1) not in hash :
                count = 1
                while (n+count) in hash :
                    count+=1
                longest = max(count, longest)
        return longest
        

        