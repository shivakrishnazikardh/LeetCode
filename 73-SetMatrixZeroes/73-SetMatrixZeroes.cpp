// Last updated: 7/28/2025, 12:51:30 PM
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        vector<vector<int>> v;
        for (int i = 0; i < matrix.size(); i++){
            for (int j = 0; j < matrix[0].size(); j++){
                if (matrix[i][j] == 0){
                    v.push_back({i,j});
                    
                }
            }
        }

        for (int z = 0; z < v.size(); z++){
            for (int x = 0; x < matrix.size(); x++){
                matrix[x][v[z][1]] = 0;
            }
            for (int x = 0; x < matrix[0].size(); x++){
                matrix[v[z][0]][x] = 0;
            }
        }
        

        
    }
};