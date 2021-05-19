class Solution:
    def __init__(self):
        self.decode=dict(zip([i+1 for i in range(26)],list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")))
        self.memo={}
        self.s=None
      
    def recursion(self,acum,i):
        auxi=acum[:]
        if i>=len(self.s):
            return 1
        if self.s[:i] in self.memo:
            return self.memo[self.s[:i]]
        else:
            a=0
            b=0
            if self.s[i]!='0':
                ax=auxi[:]
                ax.append(self.s[i])
                a=self.recursion(ax,i+1)
                if i+1<len(self.s):
                    if int(self.s[i]+self.s[i+1])<=26:
                        ax=auxi[:]
                        ax.append(self.s[i]+self.s[i+1])
                        b=self.recursion(ax,i+2)
            result=a+b
            self.memo[self.s[:i]]=result
        return result  

    def numDecodings(self, s: str) -> int:
        self.s=s
        r=self.recursion([],0)
        return r
