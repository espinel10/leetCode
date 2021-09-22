#https://leetcode.com/problems/permutation-in-string/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=sorted(s1)
        band=0
        for i in range(len(s2)-len(s1)+1):
            a=s2[i:i+len(s1)]
            a=sorted(a)
            if a == s1:
                band=1
                break
        return band==1
