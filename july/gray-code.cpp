

###https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3799/
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> ans(1<<n);
        for(int i = 0 ; i < 1<<n ; i++) ans[i] = i^(i>>1);
        return ans;
    } 
};
