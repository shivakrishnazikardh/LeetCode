// Last updated: 7/28/2025, 12:51:29 PM
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> nums;
        int i=0, j=0;
        while (m>i && n>j){
            if(nums1[i]>nums2[j]){
                nums.push_back(nums2[j]);
                j++;
            }
            else{
                nums.push_back(nums1[i]);
                i++;
            }
        }

        while (m>i){
            nums.push_back(nums1[i]);
            i++;
        }
        while (n>j){
            nums.push_back(nums2[j]);
            j++;
        }
        
        nums1=nums;
        
    }
};