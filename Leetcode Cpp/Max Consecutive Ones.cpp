class Solution {
public:
        Solution() {
        ios::sync_with_stdio(0);
        cin.tie(0);
    }
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int t=0,c=0;
        for(int i:nums){
            if(i==1){
                c++;
            }
            else{
                t=max(t,c);
                c=0;
            }
        }
        t=max(t,c);
        c=0;
        return t;
    }
};