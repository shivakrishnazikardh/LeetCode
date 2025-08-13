# Last updated: 8/12/2025, 11:09:06 PM
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxar = 0

        for i, j in enumerate(heights) :
            st = i
            while stack and stack[-1][1] > j :
                ind, ht = stack.pop()
                maxar = max(maxar, ht * (i - ind))
                st = ind
            stack.append((st,j))

        for i, j in stack :
            l = len(heights)
            maxar = max(maxar, j * (l - i))
            
        return maxar