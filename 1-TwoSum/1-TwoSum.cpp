// Last updated: 7/28/2025, 12:51:35 PM
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int, int>> v;
        int s = 0, e = nums.size()-1;
        for(int i = 0; i<nums.size();i++){
            v.push_back({nums[i], i});
        }
        sort(v.begin(), v.end());

        
        while(s<e){
            if(v[s].first + v[e].first == target){
                
                return {v[s].second, v[e].second};
            }
            if(v[s].first + v[e].first > target){
                e--;
            }
            else{
                s++;
            }
        }

                
        return {-1,-1};

        
    }
};