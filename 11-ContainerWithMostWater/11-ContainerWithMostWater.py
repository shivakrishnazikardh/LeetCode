# Last updated: 8/1/2025, 12:35:19 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxL = []

        while l<r :
            area = min(height[l], height[r]) * abs(r-l)
            maxL.append(area)
            
            if height[l] < height[r] :
                l+=1
            else :
                r-=1
            
        return max(maxL)
        