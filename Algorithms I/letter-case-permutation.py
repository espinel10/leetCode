## https://leetcode.com/problems/letter-case-permutation/
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        S=[]  
        
        def isNumber(letter):
            nums=['0','1','2','3','4','5','6','7','8','9']
            return letter in nums
        
        
        def recursion(arr,i):
            if i==len(s):
                S.append(arr)
                return
            if isNumber(s[i]):
                recursion(arr+s[i],i+1)
            else:
                ext=""+s[i]
                recursion(arr+ext.upper(),i+1)
                recursion(arr+ext.lower(),i+1)
        
        recursion("",0)
        return S
