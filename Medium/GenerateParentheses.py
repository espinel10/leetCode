

######author: alejandro espinel
#####proble url:https://leetcode.com/problems/generate-parentheses/

class Solution:
    def __init__(self):
        self.n=None
        self.respuesta=[]


    def match(self,a,b):
        if a=="(" and b==")":
            return 1
        else:
            return 0
    def isBalanced(self,s):
        entrada=list(s)
        a=deque(entrada)
        b=deque()
        while a:
            value=a.pop()
            if b:
                value2=b.pop()
                if self.match(value,value2)==0:
                    b.append(value2)
                    b.append(value)
            else:
                b.append(value)
        if b:
            return False
        else:
            return True

    def recursion(self,i,cadena):
        aux=cadena
        if i==self.n:
            if self.isBalanced(aux):
                self.respuesta.append(aux)
            return
        self.recursion(i+1,aux+")")
        self.recursion(i+1,aux+"(")
        
    def generateParenthesis(self, n: int) -> List[str]:
        self.n=n*2
        if n==1:
            return ["()"]
        
        self.recursion(1,"(")

        return self.respuesta
