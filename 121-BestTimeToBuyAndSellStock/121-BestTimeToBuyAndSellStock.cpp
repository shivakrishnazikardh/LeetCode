// Last updated: 7/28/2025, 12:51:28 PM
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int min_n = INT_MAX, profit = 0;

        for(int i = 0; i<n; i++){
            min_n = min(min_n, prices[i]);
            profit = max(profit, prices[i] - min_n);
        }
        
        return profit;
    }
};