# Last updated: 7/31/2025, 4:46:33 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(numbers)) :
            if (target-numbers[i]) in hash :
                return [hash[target-numbers[i]], i+1]
                
            hash[numbers[i]] = i+1
            