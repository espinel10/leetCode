class UnionFind:
    def __init__(self,n):
        self.root=[i for i in range(n)]
        
    def find(self,x):
        while self.root[x]!=x:
            x=self.root[x]
        return x
    
    def union(self,x,y):
        rootX=self.find(x)
        rootY=self.find(y)
        if rootX == rootY: return False
        self.root[rootX]=rootY
        return True
    
    def connected(self,x,y):
        return self.find(x)==self.find(y)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1: return False
        dj=UnionFind(n)
        for a,b in edges:
            if not dj.union(a,b):
                return False
        return True
            
