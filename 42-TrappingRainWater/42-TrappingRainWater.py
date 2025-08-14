# Last updated: 8/13/2025, 11:21:35 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        area = 0
        lmax, rmax = height[l], height[r]

        while l < r :
            
            if lmax < rmax :
                l+=1
                lmax = max(lmax, height[l])
                area += lmax - height[l]
                

            else :
                r-=1
                rmax = max(rmax, height[r])
                area += rmax - height[r]
                

        return area

            
       

        return area


            

        