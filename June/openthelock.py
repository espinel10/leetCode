
class Solution:
    def sumas(self,arr,i,j):
        if arr[i]==9 and j==1:
            arr[i]=0
        elif arr[i]==0 and j==-1:
            arr[i]=9
        elif j==1:
            arr[i]=arr[i]+1
        else:
            arr[i]=arr[i]-1    
        return arr[:]
    def openLock(self, deadends: List[str], target: str) -> int:
        memo={}
        if target=="0000":
            return 0
        for i in deadends:
            memo[i]=1
        if "0000" in memo:
            return -1
        mov=[(0,1),(1,1),(2,1),(3,1),(0,-1),(1,-1),(2,-1),(3,-1)]
        ant=[[0,0,0,0]]
        memo["0000"]=1
        band=0
        cont=0
        while len(ant)>0 and band==0:
            aux=[]
            for arr in ant:
                if band==1:
                    break
                for ij in mov:
                    auxi=self.sumas(arr[:],ij[0],ij[1])
                    llave=str(auxi[0])+str(auxi[1])+str(auxi[2])+str(auxi[3])
                    if llave==target:
                        band=1
                        break
                    if llave not in memo:
                        aux.append(auxi[:])
                        memo[llave]=1
            ant=aux[:]
            cont=cont+1
        if band==1:
            return cont
        else:
            return -1
