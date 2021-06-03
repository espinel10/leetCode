/// https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3766/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<long long> vi;
#define REP(i, a, b) for (int i=a; i<b; i++);
#define MAX (int)(1*pow(10,9)+7)

class Solution {
public:
    int maxArea(int h, int w, vector<int>& horizontalCuts, vector<int>& verticalCuts) {
    sort(horizontalCuts.begin(),horizontalCuts.end());sort(verticalCuts.begin(),verticalCuts.end());
    horizontalCuts.push_back(h);
    verticalCuts.push_back(w);
    ll maxV=verticalCuts[0]%MAX;ll maxH=horizontalCuts[0]%MAX;
    for(int i=0;i<horizontalCuts.size()-1;i++){
        //cout<<horizontalCuts[i+1]<<"-"<<horizontalCuts[i]<<"="<<horizontalCuts[i+1]-horizontalCuts[i]<<endl;
        ll val=((horizontalCuts[i+1]%MAX)-(horizontalCuts[i]%MAX)%MAX);
        if (val>maxH){maxH=val;}
    }
    //cout<<"--------"<<endl;
    for(int i=0;i<verticalCuts.size()-1;i++){
        //cout<<verticalCuts[i+1]<<"-"<<verticalCuts[i]<<"="<<verticalCuts[i+1]-verticalCuts[i]<<endl;
        ll val=((verticalCuts[i+1]%MAX)-(verticalCuts[i]%MAX))%MAX;
        if (val>maxV){maxV=val;}
    }

    ll resultado=(maxV*maxH)%MAX;
    return resultado;
    }
};
