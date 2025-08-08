# Last updated: 8/7/2025, 11:00:58 PM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0]*len(temperatures)

        for i in range(len(temperatures)):

            

            while stack and temperatures[stack[-1]] < temperatures[i]:
                answer[stack[-1]] = (i - stack[-1])
                stack.pop()
            

            stack.append(i)

        return answer
        