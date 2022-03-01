class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0] * n
        
    def find(self, x):
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
                      
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        from collections import defaultdict
        ds=UnionFind(len(s))
        
        for e in pairs:
            ds.union(e[0],e[1])
        
        d=defaultdict(list)
        d2=defaultdict(str)
        
        for i in range(len(s)):
            key=ds.find(i)
            d[key].append(i)
            d2[key]+=s[i]
            
        s=list(s)
        for key,indices in d.items():
            text=d2[key]
            text=sorted(text)
            for j in range(len(indices)):
                s[indices[j]]=text[j]
        
        return "".join(s)
        
