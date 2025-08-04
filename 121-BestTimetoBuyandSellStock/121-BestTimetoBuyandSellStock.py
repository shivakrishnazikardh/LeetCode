# Last updated: 8/4/2025, 9:47:13 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        prof = 0

        while sell < len(prices):
            if prices[buy] < prices[sell] :
                m = prices[sell] - prices[buy]
                prof = max(m, prof)
            else :
                buy = sell
            sell += 1
        return prof