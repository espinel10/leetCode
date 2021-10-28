#Number of Provinces
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX
                    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        dj=UnionFind(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]==1:
                    dj.union(i,j)
        return len(set(dj.root))
