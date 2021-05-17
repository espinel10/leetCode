import re

class Solution:
    def __init__(self):
        self.salida=False
        self.m=None
        self.n=None
        self.board=None
    
    def recursion(self,ruta,palabra):
        mov=[]
        i,j=ruta[-1][0],ruta[-1][1]
        if j-1>-1:
            mov.append([i,j-1])
        if j+1<self.n:
            mov.append([i,j+1])
        if i-1>-1:
            mov.append([i-1,j])
        if i+1<self.m:
            mov.append([i+1,j])
        
        for k in mov:
            if self.board[k[0]][k[1]]==palabra[0] and k not in ruta and self.salida==False:
                aux=ruta[:]
                aux.append(k[:])
                w=palabra[:]
                w.pop(0)
                if len(w)==0:
                    self.salida=True
                    break
                else:
                    self.recursion(aux,w)
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        word=list(word)
        self.m=len(board)
        self.n=len(board[0])
        self.board=board
        
        if self.m==1:
            w="".join(word)
            b="".join(board[0])
            m=re.findall(w,b)
            if len(m)>0:
                return True
            else:
                b=b[::-1]
                m=re.findall(w,b)
                if len(m)>0:
                    return True
                else:
                    return False
            

 
        for i in range(self.m):
            if self.salida==True:
                break
            for j in range(self.n):
                if board[i][j]==word[0]:
                    aux=[[i,j]]
                    auxi=word[:]
                    auxi.pop(0)
                    if len(auxi)==0:
                        self.salida=True
                        break
                    self.recursion(aux,auxi)
                    
        return self.salida    
