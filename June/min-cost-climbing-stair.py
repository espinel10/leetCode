class Solution:
    def __init__(self):
        self.F=None
        self.cost=None
        
    def recursion(self,i):
        if i==len(self.cost)-2 or i==len(self.cost)-1:
            self.F[i]=self.cost[i]
            return self.cost[i]
        
        if self.F[i]==-1:
            self.F[i]=self.cost[i]+min(self.recursion(i+1),self.recursion(i+2)) 
        return self.F[i]
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==2:
            return min(cost)
        self.F=[-1 for i in range(len(cost))]
        self.cost=cost
        F=self.recursion(0)
        return min(self.F[0],self.F[1])
