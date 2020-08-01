

class Solution {
public:

    Solution(){
        std::ios::sync_with_stdio(false);
        std::cin.tie(NULL);
        std::cout.tie(NULL);
        }

    bool containsDuplicate(vector<int>& nums){
        int z=nums.size();
        if(z==0 or z==1){
            return false;
        }
        sort(nums.begin(),nums.end());
        for(int i=0;i<z-1;i++){
            if(nums[i]==nums[i+1]){
                return true;
            }
       
        }
             return false;
        }
    };