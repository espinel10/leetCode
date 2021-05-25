////url https://leetcode.com/problems/number-of-islands/



#include <bits/stdc++.h>
using namespace std;
struct Node {int y, x;};
class Solution {
  public:
  int cont=0;
  vector<vector<int>>mapa;



public:
    void mostrar(){
        for(int i=0;i<mapa.size();i++){
            for(int j=0;j<mapa[0].size();j++){
                cout<<mapa[i][j]<<" ";
            }
            cout<<endl;
        }
        
    }
    
    
    void recursion(int y,int x){
    mapa[y][x]=cont;    
    if(y+1<mapa.size()){if(mapa[y+1][x]==-1){recursion(y+1,x);}}
    if(y-1>-1){if(mapa[y-1][x]==-1){recursion(y-1,x);}}
    if(x+1<mapa[0].size()){if(mapa[y][x+1]==-1){recursion(y,x+1);}}
    if(x-1>-1){if(mapa[y][x-1]==-1){recursion(y,x-1);}}
    }

    int numIslands(vector<vector<char>>& grid) {
    vector<int>algo;
    vector<Node> terr;
    for(int i=0;i<grid[0].size();i++){algo.push_back(0);}
    for(int j=0;j<grid.size();j++){mapa.push_back(algo);}
      for(int i=0;i<grid.size();i++){
        for(int j=0;j<grid[0].size();j++){
          if(grid[i][j]=='1'){mapa[i][j]=-1;terr.push_back({i,j});}
        }
       }
     
        for(auto v:terr){
          if(mapa[v.y][v.x]==-1){recursion(v.y,v.x);cont++;}
         //mostrar();
         //   cout<<"siguiente";
         }
        
      return cont;    
      }
};






int main(){
obj=Solution();
return 0;
}
