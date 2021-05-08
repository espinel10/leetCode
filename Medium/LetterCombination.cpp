#include <bits/stdc++.h>
using namespace std;
#include <math.h>  
#include <string.h>
#include <map>
#include <vector>



//////https://leetcode.com/problems/letter-combinations-of-a-phone-number



class Solution {
public:
map<char,string>phone;
vector<string>salida;
string digitos;


public:
    void recursion(int j,string cadena){
        if(cadena.size()==digitos.size()){
        salida.push_back(cadena);
        }else{
            string letters=phone[digitos[j]];
            for(int i=0;i<letters.size();i++){
                char letter=letters[i];
                string new_cadena=cadena;
                new_cadena.push_back(letter);
                recursion(j+1,new_cadena);
            }
        }
    }

    vector<string> letterCombinations(string digits) {
        if(digits.size()==0){
        return salida;    
        }
        phone['2']="abc";
        phone['3']="def";
        phone['4']="ghi";
        phone['5']="jkl";
        phone['6']="mno";
        phone['7']="pqrs";
        phone['8']="tvu";
        phone['9']="wxyz";
        digitos=digits;
        recursion(0,"");
    return salida;
        
    }
};

int main(){
    Solution obj;
    vector<string> algo=obj.letterCombinations("23");

    return 0;
}