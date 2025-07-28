# Last updated: 7/28/2025, 12:51:34 PM
class Solution(object):
    def twoSum(self, nums, target):
        hashmp = {}
        
        for i, j in enumerate(nums) :
            diff = target - j
            if diff in hashmp :
                return [hashmp[diff], i]
            hashmp[j] = i
                
        