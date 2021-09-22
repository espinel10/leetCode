##https://leetcode.com/problems/flood-fill/

class Solution:
    def __init__(self):
        self.image=None
        self.newColor=None
        self.memo={}
        
    def recursion(self,i,j,ant):
        if self.image[i][j]==ant:
            self.memo[str(i)+str(j)]=1
            self.image[i][j]=self.newColor
        if i-1>=0:
            if self.image[i-1][j]==ant:
                if str(i-1)+str(j) not in self.memo:
                    self.recursion(i-1,j,ant)
        if i+1<len(self.image):
            if self.image[i+1][j]==ant:
                if str(i+1)+str(j) not in self.memo:
                    self.recursion(i+1,j,ant)
        if j-1>=0:
            if self.image[i][j-1]==ant:
                if str(i)+str(j-1) not in self.memo:
                    self.recursion(i,j-1,ant)         
        if j+1<len(self.image[0]):
            if self.image[i][j+1]==ant:
                if str(i)+str(j+1) not in self.memo:
                    self.recursion(i,j+1,ant)
  
        
        
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.image=image[:][:]
        self.newColor=newColor
        ant=self.image[sr][sc]
        self.image[sr][sc]=self.newColor
        self.recursion(sr,sc,ant)
        return self.image
        
