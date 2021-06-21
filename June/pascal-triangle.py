class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        salida=[[1]]
        if numRows==1:
            return salida
        salida.append([1,1])
        numRows=numRows-2
        for i in range(numRows):
            aux=[1]
            for j in range(0,len(salida[-1])-1):
                aux.append(salida[-1][j]+salida[-1][j+1])
            aux.append(1)
            salida.append(aux)
        return salida
