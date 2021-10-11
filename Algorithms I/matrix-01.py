##https://leetcode.com/problems/01-matrix/
class Solution:
    def updateMatrix(self, mat):
        def isZeroNear(i,j):
            for a,b in [(i+1,j),(i-1 ,j),(i,j+1),(i,j-1)]:
                if 0 <= a < len(mat) and 0 <= b < len(mat[0]):
                    if mat[a][b] == 0:
                        return True
            return False
        
        edges = set()
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1  and isZeroNear(i,j):
                    edges.add((i , j , 1))
        
        visited = set()
        queue = edges
        
        while queue:
            temp = set()
            for i,j,v in queue:
                if (i,j) in visited:
                    continue
                visited.add((i,j))
                mat[i][j] = v
                for a,b in [(i+1,j),(i-1 ,j),(i,j+1),(i,j-1)]:
                    if 0 <= a < len(mat) and 0 <= b < len(mat[0]) and mat[a][b]==1 and (a,b) not in visited:
                        temp.add((a,b, v +1))
            queue = temp
        
        return mat            
                
