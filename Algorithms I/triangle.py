class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo={}
        def recursion(nums,i,ref):
            if i==len(nums):
                return 0
            cont=0
            if ref not in memo:
                j=int(ref.split(":")[1])
                memo[ref]=nums[i][j]+min(recursion(nums,i+1,str(i)+":"+str(j)),recursion(nums,i+1,str(i)+":"+str(j+1)))
            return memo[ref]    
        return recursion(triangle,0,"0:0")
