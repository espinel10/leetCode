
##########https://leetcode.com/problems/find-the-town-judge




class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust)==0:
            if N==1:
                return 1
            else:
                return -1
        
        val=[0 for i in range(N)]
        val2=[0 for i in range(N)]
 
        for i in trust:
            val[i[1]-1]=val[i[1]-1]+1
            val2[i[0]-1]=val2[i[0]-1]+1

        maxi=max(val)
        j=val.index(maxi)
        if val2[j]==0 and maxi==N-1:
            return j+1
        else:
            return -1