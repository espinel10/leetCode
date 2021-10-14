# https://leetcode.com/problems/house-robber/
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        def recursion(nums,i):
            if i>=len(nums)-1:
                if i==len(nums)-1:
                    return nums[i]
                else:
                    return 0
            cont=0
            if i not in memo:
                a,b=recursion(nums,i+2),recursion(nums,i+3)
                cont=nums[i]+max(a,b)
                memo[i]=cont
            else:
                cont=memo[i]
            return cont
        return max(recursion(nums,0),recursion(nums,1))
