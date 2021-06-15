class Solution:
    def __init__(self):
        self.bandera=False
        self.side=0

    def recursion(self,A,B,C,D,stks):
        sticks=stks[:]
        if len(sticks)==0:
            if A==B==D==C:
                self.bandera=True
            return 
        num=sticks[0]
        sticks.pop(0)
        if self.bandera==False and A+num <=self.side:
            self.recursion(A+num,B,C,D,sticks[:])
        if self.bandera==False and B+num <=self.side:
            self.recursion(A,B+num,C,D,sticks[:])
        if self.bandera==False and C+num <=self.side:
            self.recursion(A,B,C+num,D,sticks[:])
        if self.bandera==False and D+num <=self.side:
            self.recursion(A,B,C,D+num,sticks[:])    
    
    def makesquare(self, matchsticks: List[int]) -> bool:
        per=sum(matchsticks)
        if per%4!=0:
            return False
        else:
            self.side=per//4
        matchsticks=sorted(matchsticks,reverse=True)
        self.recursion(0,0,0,0,matchsticks)
        return self.bandera
 
