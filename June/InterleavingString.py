class Solution:
    def __init__(self):
        self.memo={}
    def recursion(self,s1,s2,s3):
        if s3=="":
            if s1=="" and s2=="":
                return True
            return False
        llave=str(s1)+":"+str(s2)+":"+str(s3)
        if llave in self.memo:
            return self.memo[llave]
        A=False
        B=False
        if s1!="":
            if s1[0]==s3[0]:
                A=self.recursion(s1[1:],s2[:],s3[1:])
        if s2!="":
            if s2[0]==s3[0]:
                B=self.recursion(s1[:],s2[1:],s3[1:])
        self.memo[llave]=A|B
        return self.memo[llave]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        resp=self.recursion(s1,s2,s3)
        return resp
