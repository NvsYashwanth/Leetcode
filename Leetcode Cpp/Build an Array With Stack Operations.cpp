class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> res;
        int count = 1;
        for (int i = 0; i < target.size();){
            while(target[i] != count){
                res.push_back("Push");
                res.push_back("Pop");
                count++;
            }
            res.push_back("Push");
            i++;
            count++;
        }
        return res;
    }
};