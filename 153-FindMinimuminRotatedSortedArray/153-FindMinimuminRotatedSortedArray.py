# Last updated: 8/14/2025, 9:37:42 PM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        
        min_n = nums[0]
       
        while start <= end  :

            if nums[start] <= nums[end] :
                min_n = min(min_n, nums[start])
                break

            else :
                mid = (start + end) // 2
                min_n = min(min_n, nums[mid])

                if nums[mid] >= nums[end] :
                    start = mid + 1

                else :
                    end = mid -1

        return min_n
            
            

        