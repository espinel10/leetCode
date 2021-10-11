# https://leetcode.com/problems/rotting-oranges/
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        cont=-1
        queue=set()
        ref=set()
        
        def isOneNear(i,j):
            for a,b in [(i+1,j),(i-1 ,j),(i,j+1),(i,j-1)]:
                if 0 <= a < len(grid) and 0 <= b < len(grid[0]):
                    if grid[a][b]==1:
                        return True
            return False
                    
        
        edges=set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2 and isOneNear(i,j):
                    edges.add((i,j)) 
                if grid[i][j]==1:
                    ref.add((i,j))
                    
        if len(queue)==0 and len(ref)==0:
            return 0
                    
        visited=set()
        queue = edges
        while queue:
            temp=set()
            for i,j in queue:
                if (i,j) in visited:
                    continue
                visited.add((i,j))
                grid[i][j]=2
                for a,b in [(i+1,j),(i-1 ,j),(i,j+1),(i,j-1)]:
                    if 0 <= a < len(grid) and 0 <= b < len(grid[0]) and grid[a][b]==1 and (a,b) not in visited and (a,b) not in queue:
                        temp.add((a,b))
            queue = temp
            cont+=1
            
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        return cont
