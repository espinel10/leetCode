##https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        memo[1]=1
        memo[2]=2
        memo[3]=3
        def recursion(n):
            if n==0:
                return 0
            cont=0
            if n not in memo:
                a=recursion(n-1)
                b=recursion(n-2)
                cont=a+b
                memo[n]=cont
            else:
                cont=memo[n]
            return cont
        return recursion(n)
