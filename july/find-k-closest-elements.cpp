////https://leetcode.com/problems/find-k-closest-elements/solution/

class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        stable_sort(begin(arr), end(arr), [x](int a, int b){
            return abs(a - x) < abs(b - x);   
        });
        arr.resize(k);                      
        sort(begin(arr), end(arr));           
        return arr; 
    }
};
