class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
          vector<int> t(arr);
        sort(t.begin(), t.end());
        
        unordered_map<int, int> map;
        for(int i = 0, rank = 1; i < t.size(); i++) {
            if(i == 0 || t[i] != t[i-1]) {
                map[t[i]] = rank++;
            }
        }
        
        vector<int> res;
        for(int i = 0; i < arr.size(); i++) res.push_back(map[arr[i]]);
        return res;
    }
    };
