# Last updated: 8/16/2025, 5:30:58 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        res = -1
        mid = (start + end)//2

        while start <= end :

            if nums[mid] == target :
                return mid

            if nums[start] <= nums[mid] :
                if target < nums[mid] and target >= nums[start] :
                    end = mid - 1
                else :
                    start = mid + 1
            else :
                if target < nums[mid] or target >= nums[start] :
                    end = mid - 1
                else :
                    start = mid + 1

            mid = (start+end)//2

        return res


            