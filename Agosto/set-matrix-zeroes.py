
#https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3888/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        xy=[]
        zeros=[0]*len(matrix[0])
        for j in range(len(matrix)):
            for i in range(len(matrix[0])):
                if matrix[j][i]==0:
                    xy.append((j,i))
        for ij in xy:
            for k in range(len(matrix)):
                matrix[k][ij[1]]=0
  
        for ij in xy:
            matrix[ij[0]]=zeros[:]
