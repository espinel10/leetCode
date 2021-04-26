///////https://leetcode.com/problems/valid-anagram


#include <bits/stdc++.h>
using namespace std;
#include <vector>
#include <string> 
#include <map>
#include <math.h>  

class Solution {
public:
    bool isAnagram(string s, string t) {
     int zero[26]={0};
        
        for( int i=0;i< s.size();i++){
            zero[s[i]-'a']++;     
        }

        for( int i=0;i< t.size();i++){
            zero[t[i]-'a']--;
        }
        for(int i=0;i<26;i++){
            if(zero[i]!=0){
                return false;
            }
        }
        return true;
    }
        
    
};



int main(){
string s,t;
cin >>s;
cin >>t;
Solution obj;
cout << obj.isAnagram(s,t);

return 0;    
}