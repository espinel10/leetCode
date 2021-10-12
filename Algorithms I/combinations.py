# https://leetcode.com/problems/combinations/
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations=[]
        
        def backtrack(first=1,curr=[]):
            # if the combinations is done
            if len(curr)==k:
                combinations.append(curr[:])
            for i in range(first,n+1):
                curr.append(i)
                backtrack(i+1,curr)
                curr.pop()

        backtrack()
        return combinations
            
