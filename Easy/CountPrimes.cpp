///////https://leetcode.com/problems/count-primes/


#include <bits/stdc++.h>
using namespace std;
#include <math.h>  

class Solution {
public:
    int countPrimes(int n) {
        if(n<=2){
           return 0; 
        }

        int primes[n];
        for(int i=0;i<n;i++){
        primes[i]=-1;
        }
        for(int i=2;i<=sqrt(n);i++){
        if(primes[i]==-1){

          for(int j=i;j<n;j=j+i){
              if(i==j){
                  continue;
              }
              primes[j]=1;
          }      
        }else{
            continue;
        }

        }           
        int cont=0;
        for(int i=2;i<n;i++){
            if(primes[i]==-1){   
            cont++;
            }
        }
    
        return cont;
        }
        
    
};



int main(){
int n;
cin >>n;
Solution obj;
cout << obj.countPrimes(n)<<endl;

return 0;    
}