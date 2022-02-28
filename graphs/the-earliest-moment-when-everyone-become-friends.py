class UnionFind:
    
    def __init__(self,n):
        self.root=[i for i in range(n)]
    
    def find(self,x):
        return self.root[x]
        
    def union(self,x,y):
        
        rootX=self.find(x)
        rootY=self.find(y)
        
        if rootX!=rootY:
            for i in range(len(self.root)):
                if self.root[i]==rootY:
                    self.root[i]=rootX


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs=sorted(logs,key=lambda x:x[0])
        dj=UnionFind(n)
        i=0
        while len(set(dj.root))>1 and i<len(logs):
            dj.union(logs[i][1],logs[i][2])
            i=i+1
       
        if len(set(dj.root))!=1:
            return -1
    
        return logs[i-1][0]
        
        
        
