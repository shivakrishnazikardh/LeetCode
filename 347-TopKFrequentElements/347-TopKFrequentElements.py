# Last updated: 7/28/2025, 12:51:25 PM
class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        for i, j in count.items():
            freq[j].append(i)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res

         