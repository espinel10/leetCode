#https://leetcode.com/problems/power-of-two/
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i=0
        while (1<<i) < n:
            i+=1
        if (1<<i) ==n:
            return True
        return False
