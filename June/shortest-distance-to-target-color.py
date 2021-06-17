class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        values=[[-1,-1,-1] for i in range(len(colors))]
        memo=dict(zip([1,2,3],[-1,-1,-1]))
        for i in range(len(colors)):
            memo[colors[i]]=0
            aux=[1,2,3]
            aux.remove(colors[i])
            if memo[aux[0]]!=-1:
                memo[aux[0]]=memo[aux[0]]+1
            if memo[aux[1]]!=-1:
                memo[aux[1]]=memo[aux[1]]+1
            values[i][0]=memo[1]
            values[i][1]=memo[2]
            values[i][2]=memo[3]
        values2=[[-1,-1,-1] for i in range(len(colors))]
        memo=dict(zip([1,2,3],[-1,-1,-1]))
        for i in range(len(colors)-1,-1,-1):
            memo[colors[i]]=0
            aux=[1,2,3]
            aux.remove(colors[i])
            if memo[aux[0]]!=-1:
                memo[aux[0]]=memo[aux[0]]+1
            if memo[aux[1]]!=-1:
                memo[aux[1]]=memo[aux[1]]+1
            values2[i][0]=memo[1]
            values2[i][1]=memo[2]
            values2[i][2]=memo[3]
        salida=[]
        for query in queries:
            num=-1
            a=values[query[0]][query[1]-1]
            b=values2[query[0]][query[1]-1]
            if min(a,b)!=-1:
                num=min(a,b)
            else:
                num=max(a,b)
            salida.append(num)
        return salida
