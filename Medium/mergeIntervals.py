class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda x:x[0])
        salida=[intervals[0]]
        for i in intervals:
            if i[0]<=salida[-1][1]:
                if i[1]>salida[-1][1]:
                    salida[-1][1]=i[1]
            else:
                salida.append(i)
        return salida
        
