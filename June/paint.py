class Solution:
    def __init__(self):
        self.costs=None
        self.memo={}

    def recursion(self,ant,j):
        if j==len(self.costs)-1:
            aux=self.costs[-1][:]
            aux[ant]=100000
            return min(aux)
        ptr=[0,1,2]
        if ant!=-1:
            ptr.remove(ant)
        val=[]
        for it in ptr:
            llave=str(j)+":"+str(it)+":"+str(self.costs[j][it])
            if llave in self.memo:
                val.append(self.memo[llave])
            else:
                num=self.costs[j][it]+self.recursion(it,j+1)
                self.memo[llave]=num
                val.append(num)
        return min(val)           
    def minCost(self, costs: List[List[int]]) -> int:
        self.costs=costs
        if len(self.costs)==1:
            return min(self.costs[0])
        respuesta=self.recursion(-1,0)
        return respuesta
