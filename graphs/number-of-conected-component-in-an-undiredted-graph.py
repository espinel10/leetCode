class UnionFind:
    
    def __init__(self,n):
        self.root=[i for i in range(n)]
        self.n=n
        
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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dj=UnionFind(n)
        for e in edges:
            dj.union(e[0],e[1])
        return len(set(dj.root))
