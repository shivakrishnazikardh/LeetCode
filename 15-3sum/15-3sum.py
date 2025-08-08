# Last updated: 8/7/2025, 11:01:08 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trip = []
        nums.sort()
        for i, j in enumerate(nums):
            if i > 0 :
                if j == nums[i-1] :
                    continue
            l, r = i+1, len(nums)-1
            while l<r :
                threeS = j + nums[l] + nums[r]
                if threeS > 0 :
                    r -= 1
                   
                elif threeS < 0 :
                    l += 1
                    
                else :
                    trip.append([j, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return trip


