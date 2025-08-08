# Last updated: 8/7/2025, 11:01:04 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0

        for i in range(len(prices)) :
            if prices[i] < buy or i == 0:
                buy = prices[i]
            if (prices[i] - buy) > sell :
                sell = prices[i] - buy

        return sell