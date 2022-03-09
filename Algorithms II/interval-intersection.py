##https://leetcode.com/problems/interval-list-intersections


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result=[]
        i,j=0,0
        while i<len(firstList) and j<len(secondList):
            a,b,c,d=firstList[i][0],firstList[i][1],secondList[j][0],secondList[j][1]
            if max(b,d)==b:
                if a<= d <=b:
                    x,y=d,d
                    if a<=c<=b:
                        x=c
                    if c<=a<=b:
                        x=a
                    result.append([x,y])
                j+=1
            else:
                if c<=b<=d:
                    x,y=b,b
                    if c<=a<=d:
                        x=a
                    if a<=c<=d:
                        x=c
                    result.append([x,y])
                i+=1
        return result    
