//////////////////https://leetcode.com/problems/happy-number/
#include <bits/stdc++.h>
using namespace std;
#include <vector>
#include <string> 
#include <map>
#include <math.h>  
class Solution {
public:
    bool isHappy(int n) {
    bool bandera=true;
    map<int,int>history;
    while(bandera==true){
        int aux=n;
        int acum=0;
        while(aux>0){
            int dig=aux%10;
            aux=aux/10;
            acum=acum+pow(dig,2);
        }
        if (acum==1 or history.count(acum)>0){
            bandera=false;
        }else{
        history[acum]=acum;
        }
        n=acum;
    }
    if(n==1){
        return true;
    }else{
        return false;
    }    

        
    }
};


int main(){
int n;
cin >>n;
Solution obj;
obj.isHappy(n);


return 0;    
}