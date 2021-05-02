#include <bits/stdc++.h>
using namespace std;
#include <vector>
#include <string> 
#include <map>
#include <math.h>  


class Logger {
public:
    /** Initialize your data structure here. */
    map<string,int>tabla;
    Logger() {
    
        
    }
    
    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    bool shouldPrintMessage(int timestamp, string message) {

        if(tabla.count(message)==0){
            tabla[message]=timestamp;
            return true;
        }

        if (timestamp - tabla[message] >=10){
        tabla[message]=timestamp;
        return true;
        }else{
            return false;
        }

        
    }
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger* obj = new Logger();
 * bool param_1 = obj->shouldPrintMessage(timestamp,message);
 */