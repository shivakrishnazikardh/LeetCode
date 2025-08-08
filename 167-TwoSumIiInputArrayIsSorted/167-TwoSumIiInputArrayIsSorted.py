# Last updated: 8/7/2025, 11:01:01 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''hash = {}
        for i in range(len(numbers)) :
            if (target-numbers[i]) in hash :
                return [hash[target-numbers[i]], i+1]
                
            hash[numbers[i]] = i+1'''

        l, r = 0, len(numbers)-1

        while l < r :
            if numbers[l] + numbers[r] == target :
                return [l+1, r+1]
            if numbers[l] + numbers[r] > target :
                r -= 1
            if numbers[l] + numbers[r] < target :
                l += 1
            