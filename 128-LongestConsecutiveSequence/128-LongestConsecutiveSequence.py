# Last updated: 7/29/2025, 10:27:04 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''hash = set(nums)
        longest = 0

        for n in nums :
            if (n-1) not in hash :
                count = 1
                while (n+count) in hash :
                    count+=1
                longest = max(count, longest)
        return longest'''
        longest = 0
        num_set = set(nums)

        for n in num_set:
            if (n-1) not in num_set:
                length = 1
                while (n+length) in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest

        