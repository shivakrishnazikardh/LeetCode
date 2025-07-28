# Last updated: 7/28/2025, 12:51:27 PM
class Solution(object):
    def productExceptSelf(self, nums):
        ''' answer = []
        for i in range(len(nums)):
            if i == 0 :
                pre = 1
                answer.append(pre)
                continue
            if i == len(nums):
                answer.append(pre)
                break
            tem = pre * nums[i-1]
            answer.append(tem)
            pre = tem

        for j in range(len(nums)-1, -1, -1):
            if j == 0:
                tans = pos * nums[j+1]
                answer[j] = tans
                break
            if j == len(nums)-1 :
                pos = 1
                tans = pos * answer[j]
                answer[j] = tans
                continue
            tem = pos * nums[j+1]
            tans = tem * answer[j]
            answer[j] = tans
            pos = tem

        return answer '''

        answer = [1] * (len(nums))

        pre = 1
        for i in range(len(nums)):
            answer[i] = pre
            pre *= nums[i]

        pos = 1
        for j in range(len(nums)-1, -1, -1):
            answer[j] *= pos
            pos *= nums[j]
            
        return answer
            
            
        