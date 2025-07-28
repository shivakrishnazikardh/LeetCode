# Last updated: 7/28/2025, 12:51:24 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums)-1
        m = (s+e)//2

        while(s<=e):
            if(nums[m]==target):
                return m
            elif(target > nums[m]):
                s = m+1
                m = (s+e)//2
            elif(target < nums[m]):
                e = m-1
                m = (s+e)//2

        return -1 