# Last updated: 8/13/2025, 5:47:30 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        
        while start <= end :
            mid = (end + start)//2
            if nums[mid] == target :
                return mid
            elif nums[mid] > target :
                end = mid - 1 
                
            else :
                start = mid + 1
                
        return -1