// Last updated: 7/28/2025, 12:51:22 PM
class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        int s=0, e=nums.size()-1;
        int m=(s+e)/2;

        while(s<=e){
            if(target == nums[m]){
                return m;
            }
            else if(target > nums[m]){
                s = m+1;
            }
            else{
                e = m-1;
            }
            m=(s+e)/2;
        }

        return -1;
    }
};